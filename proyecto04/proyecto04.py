import pyspark
from pypark.ml.clustering import KMeans
from __future__ import print_function

import sys

from pyspark import SparkContext
from pyspark.mllib.feature import Word2Vec

USAGE = ("bin/spark-submit --driver-memory 4g "
         "examples/src/main/python/mllib/word2vec.py text8_lines")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(USAGE)
        sys.exit("Argument for file not provided")
    file_path = sys.argv[1]
    sc = SparkContext(appName='Word2Vec')
    inp = sc.textFile(file_path).map(lambda row: row.split(" "))

    word2vec = Word2Vec()
    model = word2vec.fit(inp)

    synonyms = model.findSynonyms('china', 40)

    for word, cosine_distance in synonyms:
        print("{}: {}".format(word, cosine_distance))
    sc.stop()
