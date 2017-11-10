from math import*
import numpy as np
from mpi4py import MPI

def jaccard_similarity(x,y):
    comm = MPI.COMM_WORLD
    rank = comm.rank
    size = comm.size

    if rank == 0:
        intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
        #print(intersection_cardinality)
        union_cardinality = len(set.union(*[set(x), set(y)]))
        #print(list(set.union(*[set(x), set(y)])))
        return intersection_cardinality/float(union_cardinality)

