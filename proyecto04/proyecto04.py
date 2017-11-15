from _future_ import print_function

from pyspark import SparkContext
# $example on$                                                                                                                                                                    
from pyspark.mllib.feature import HashingTF, IDF
# $example off$                                                                                                                                                                   

if _name_ == "_main_":
    sc = SparkContext(appName="TFIDFExample")  # SparkContext                                                                                                                     

    # $example on$                                                                                                                                                                
    # Load documents (one per line).                                                                                                                                              
    documents = sc.textFile("hdfs:///datasets/gutenberg-txt-es/12368.txt").map(lambda line: line.split(" "))

    hashingTF = HashingTF()
    tf = hashingTF.transform(documents)

    # While applying HashingTF only needs a single pass to the data, applying IDF needs two passes:                                                                               
    # First to compute the IDF vector and second to scale the term frequencies by IDF.                                                                                            
    tf.cache()
    idf = IDF().fit(tf)
    tfidf = idf.transform(tf)

    # spark.mllib's IDF implementation provides an option for ignoring terms                                                                                                      
    # which occur in less than a minimum number of documents.                                                                                                                     
    # In such cases, the IDF for these terms is set to 0.                                                                                                                         
    # This feature can be used by passing the minDocFreq value to the IDF constructor.                                                                                            
    idfIgnore = IDF(minDocFreq=2).fit(tf)
    tfidfIgnore = idfIgnore.transform(tf)
    # $example off$                                                                                                                                                               

    print("tfidf:")
    carpeta = open("tfidf.txt","w")
    for each in tfidf.collect():
        print(each)
        carpeta.write(str(each))

    print("tfidfIgnore:")
    for each in tfidfIgnore.collect():
        print(each)

    sc.stop()
