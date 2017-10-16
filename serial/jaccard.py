from math import*
import numpy as np

def jaccard_similarity(x,y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    #print(intersection_cardinality)
    union_cardinality = len(set.union(*[set(x), set(y)]))
    #print(list(set.union(*[set(x), set(y)])))
    return intersection_cardinality/float(union_cardinality)


