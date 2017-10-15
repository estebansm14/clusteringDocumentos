#  Clústering de Documentos a partir de Métricas de Similitud

Integrantes del grupo:
Ana María Bedoya Hernández - abedoy19@eafit.edu.co
Esteban Salazar Montoya - esalaza7@eafit.edu.co

## 1. Descripción del proyecto:
Este proyecto hace parte de la asignatura Tópicos Especiales en Telemática. Este consiste en diseñar e implementar un algoritmo paralelo que permita agrupar (clustering) un conjunto de documentos utilizando el algoritmo de k–means y una métrica de similaridad entre documentos.

## 2. Modo de ejecución:
Para ejecutar el programa se deben ejecutar los siguientes comandos en la terminal:

Para el algoritmo serial:

		$ python serial/proyecto3.py ../ruta en donde esté la carpeta con el dataset

Para el algoritmo paralelo:

		$ mpiexec -np 4 python paralelo/proyectoParalelo.py ../ruta en donde esté la carpeta con el dataset

## 3. Algoritmos utilizados:
* Jaccard: Fue empleado para conocer la similaridad entre documentos.
* K-means: Fue el método de agrupamiento empleado entre los documentos una vez se calculara el grado de similaridad entre estos.

## 4. Requisitos:
* Tener MPI instalado.
* Tener Python instalado, recomendada la versión 2.7

## 5. Referencias:


	



