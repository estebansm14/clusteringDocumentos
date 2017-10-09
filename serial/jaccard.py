from math import*
import numpy as np
 
def jaccard_similarity(x,y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    print(intersection_cardinality)
    union_cardinality = len(set.union(*[set(x), set(y)]))
    print(list(set.union(*[set(x), set(y)])))
        return intersection_cardinality/float(union_cardinality)

print jaccard_similarity([0,1,2],[0,2,3])

# crear la matriz

X = np.vstack((data1,np.vstack((data2,data3))))
