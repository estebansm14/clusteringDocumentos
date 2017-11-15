import re
from pyspark import SparkContext

# An even better cleanup would include stemming,
# careful punctuation removal, etc.
def clean(doc):
    sc = SparkContext(appName="TFIDFExample")
    return filter(lambda w: len(w) > 2,
                  map(lambda s: s.lower(), re.split(r'\W+', doc)))

datasets = sc.wholeTextFiles("hdfs:///datasets/gutenberg-txt-es/*.txt")    \
           .mapValues(clean)                                            \
           .cache()
essayNames = datasets.map(lambda (filename, contents): filename).collect()
docs = datasets.map(lambda (filename, contents): contents)
print docs 