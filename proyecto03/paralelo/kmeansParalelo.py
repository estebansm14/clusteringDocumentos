import numpy as np
from mpi4py import MPI

def kMeans(X, K, maxIters = 10, plot_progress = None):
    comm = MPI.COMM_WORLD
    rank = comm.rank
    size = comm.size
    name = MPI.Get_processor_name()
    if rank == 0:
        centroids = X[np.random.choice(np.arange(len(X)), K), :]
        for i in range(rank,maxIters,size):
            # Cluster Assignment step
            C = np.array([np.argmin([np.dot(x_i-y_k, x_i-y_k) for y_k in centroids]) for x_i in X])
            # Move centroids step
            centroids = [X[C == k].mean(axis = 0) for k in range(K)]
            if plot_progress != None: plot_progress(X, C, np.array(centroids))
        return np.array(centroids) , C
    """centroids = X[np.random.choice(np.arange(len(X)), K), :]
    if rank == 0:
        
        for i in range(rank,maxIters,size):
            # Cluster Assignment step
            C = np.array([np.argmin([np.dot(x_i-y_k, x_i-y_k) for y_k in centroids]) for x_i in X])
            # Move centroids step
    if rank == 1:

        for i in range(rank,maxIters,size):
            centroids = [X[C == k].mean(axis = 0) for k in range(K)]
            
    if plot_progress != None: plot_progress(X, C, np.array(centroids))
    return np.array(centroids) , C"""
