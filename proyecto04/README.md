#  Clústering de Documentos a partir de Métricas de Similitud basado en Big Data

Integrantes del grupo:

* Ana María Bedoya Hernández - abedoy19@eafit.edu.co

* Esteban Salazar Montoya - esalaza7@eafit.edu.co

* Jeniffer Maria Palacio Sandoval - jmpalaci@eafit.edu.co

## 1. Descripción del proyecto:
Este proyecto hace parte de la asignatura Tópicos Especiales en Telemática. Este consiste que por medio de Big Data agrupar un conjunto de documentos (clustering)  utilizando Spark con sus bibliotecas de K-Means y TF-IDF, para las métrica de simi\
laridad entre documentos.

## 2. Objetivos:
* Aplicar las tecnologías y modelos de programación en Big Data.
* Analizar los resultados entre un acercamiento paralelo (proyecto 3) y las tecnologías y modelos en Big Data.
* Entender los dos ambientes de supercomputación basados en HPC y Big Data, las limitaciones, software y hardware asociadas a distintos problemas computacionales que podrían sortearse a partir de herramientas y estrategias como computación paralela y big data.

## 3. Modo de ejecución:
Para ejecutar el programa se deben ejecutar los siguientes comandos en la terminal:

De manera local:

    $ spark-submit proyecto04.py <rutaDataset> <k> <maximoIteraciones>

Ejecutar en el cluster:

    $ spark-submit --master yarn --deploy-mode cluster --executor-memory 2G --num-executors proyecto04.py <rutaDataset> <k> <maximoIteraciones>

## 4. Algoritmos utilizados:
* TF-IDF (Term frequency-inverse document frequency): Es un método de vectorización de características muy utilizado en minería de texto para reflejar la importancia de un término para un documento. 
* K-means: Método de agrupamiento empleado entre los documentos una vez se calculara el grado de similaridad entre estos con TF-IDF.

## 5. Requisitos:
* Cluster con Spark y pyspark instalados

## 6. Referencias:
* "Feature Extraction and Transformation - RDD-based API - Spark 2.2.0 Documentation", Spark.apache.org, 2017. [Online]. Available: https://spark.apache.org/docs/2.2.0/mllib-feature-extraction.html. [Accessed: 01- Nov- 2017].
* "apache/spark", GitHub, 2017. [Online]. Available: https://github.com/apache/spark/blob/master/examples/src/main/python/mllib/tf_idf_example.py. [Accessed: 01- Nov- 2017].
* "apache/spark", GitHub, 2017. [Online]. Available: https://github.com/apache/spark/blob/master/examples/src/main/python/mllib/k_means_example.py. [Accessed: 19- Nov- 2017].


