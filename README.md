#  Clústering de Documentos a partir de Métricas de Similitud

Integrantes del grupo:

*Ana María Bedoya Hernández - abedoy19@eafit.edu.co

*Esteban Salazar Montoya - esalaza7@eafit.edu.co

## 1. Descripción del proyecto:
Este proyecto hace parte de la asignatura Tópicos Especiales en Telemática. Este consiste en diseñar e implementar un algoritmo paralelo que permita agrupar (clustering) un conjunto de documentos utilizando el algoritmo de k–means y una métrica de similaridad entre documentos.

## 2. Objetivos:
* Aplicar la metodología para el diseño de algoritmos paralelos (PCAM)
* Aplicar conocimientos de programación paralela usando estrategias adecuadas para resolver problemas intensivos en recursos computacionales.
* Analizar los resultados entre un acercamiento secuencial y paralelo incluyendo las distintas estrategias y tecnologías asociadas a Computación de Alto Rendimiento.
* Reducir tiempos de ejecución utilizando estrategias de desarrollo, tecnologías, herramientas y la infraestructura adecuada para ejecutar aplicaciones que requieran tiempos considerables y que de otra manera no sería posible ejecutarlos en un tiempo razonable.
* Entender las limitaciones a nivel de algoritmia, software y hardware asociadas a distintos problemas computacionales que podrían sortearse a partir de herramientas y estrategias como computación paralela y distribuida.
* Trabajar inter–disciplinariamente con otros profesionales y resolver problemas reales.

## 3. Modo de ejecución:
Para ejecutar el programa se deben ejecutar los siguientes comandos en la terminal:

Para el algoritmo serial:

		$ python serial/proyecto3.py ../ruta en donde esté la carpeta con el dataset

Para el algoritmo paralelo:

		$ mpiexec -np 4 python paralelo/proyectoParalelo.py ../ruta en donde esté la carpeta con el dataset

## 4. Algoritmos utilizados:
* Jaccard: Algoritmo empleado para conocer la similaridad entre documentos. Entre los métodos propuestos este fue el elegido debido a que según los documentos estudiados, este es uno de los más eficientes en la generación de clústers más coherentes. 
* K-means: Método de agrupamiento empleado entre los documentos una vez se calculara el grado de similaridad entre estos.

## 5. Requisitos:
* Tener MPI y mpi4py instalados.
* Tener Python instalado, recomendada la versión 2.7

## 6. Referencias:
* Anna Huang. Similarity measures for text document clustering. Proceedings of the Sixth New Zealand, (April):49–56, 2008.
* Christopher D. Manning, Prabhakar Raghavan, and Hinrich Schütze. Introduction to Information Retrieval. Cambridge University Press, 2008.
* Implementación del método de Jaccard. https://gist.github.com/ariezncahyo/7fa9c0a88b474a1b5f3b72e4d9650292
* Implementación de K-means. https://gist.github.com/bistaumanga/6023692

	



