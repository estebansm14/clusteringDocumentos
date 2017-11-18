import sys
from math import sqrt
from pyspark import SparkContext                                                                                                                                                                  
from pyspark.mllib.feature import HashingTF, IDF
from pyspark.mllib.clustering import KMeans                                                                                                                                                                   

if __name__ == "__main__":
    if len(sys.argv) <4: #Identificacion de ruta, k y maximo de iteraciones ingresados como parametro
        print("Ejecutar = spark-submit proyecto04.py <rutaDataset> <k> <maximoIteraciones>") #Imprimir si hay un fallo y se pasan parametros que no corresponden
        sys.exit(1) #El programa para
    ruta = sys.argv[1] #El primer parametro ingresado por consola corresponde a la ruta 
    k = int(sys.argv[2]) #El segundo parametro es el k
    maximoIter = int(sys.argv[3]) #El tercer parametro corresponde al maximo de iteraciones     

    sc = SparkContext(appName="Proyecto04")  # SparkContext                                                                                                                                                                                                                
    documentos = sc.wholeTextFiles(ruta) # Leer todos los archivos de la carpeta ingresada como parametro
    nombreDocumentos = documentos.keys().collect() # Nombre de los documentos
    docs = documentos.values().map(lambda doc: doc.split(" ")) # Se separan por palabras los documentos
    hashingTF = HashingTF() # Objeto tipo HashingTF
    tf = hashingTF.transform(docs) # Frecuencia de los terminos en los documentos
    idf = IDF().fit(tf) #Mide que tan relevante son los terminos en el cluster   
    tfidf = idf.transform(tf) #Resultado de la multiplicacion tfidf

    # Construye el modelo y agrupa los datos con k-means
    clusters = KMeans.train(tfidf,k,maxIterations=maximoIter) #Se obtiene el modelo k-means
    clustersid = clusters.predict(tfidf).collect() #Lista de las agrupaciones resultantes 
    diccionario = dict(zip(nombreDocumentos, clustersid)) 

    # Evaluar clustering usando algoritmo Within Set Sum of Squared Errors
    def error(point):
        center = clusters.centers[clusters.predict(point)]
        return sqrt(sum([x**2 for x in (point -center)]))

    WSSSE = tfidf.map(lambda point: error(point)).reduce(lambda x, y: x + y)
    print ("Within Set Sum of Squared Error = " + str(WSSSE))

    d = sc.parallelize(diccionario.items())
    d.coalesce(1).saveAsTextFile(rutaOut)

    sc.stop() #SparkContext detenido
