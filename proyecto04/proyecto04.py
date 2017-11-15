import re
from pyspark import SparkContext

# An even better cleanup would include stemming,
# careful punctuation removal, etc.
sc = SparkContext(appName="TFIDFExample")
def clean(doc):
    
    return filter(lambda w: len(w) > 2,
                  map(lambda s: s.lower(), re.split(r'\W+', doc)))

datasets = sc.wholeTextFiles("hdfs:///datasets/gutenberg-txt-es/*.txt")    \
           .mapValues(clean)                                            \
           .cache()
var = (filename, contents)
essayNames = datasets.map(lambda var: filename).collect()
docs = datasets.map(lambda var: contents)
essayNames.saveAsTextFile("hdfs:///user/esalaza7/practica_out")
