'''
Author: Janike Katter
Version: 12.01.2021
'''
import scipy.linalg as linalg
import numpy as np
import math

def householder_step(A, id_index=1):
    '''
    One step of the Householder Transformation. Recursively calls itself.
    ----------
    Parameter:
    ----------
    A: np.matrix
        The Matrix to be transformed
    id_index: int
        The step index
    --------
    Returns:
    --------
    H: np.matrix
        The transformed matrix
    '''
    n,m = A.shape
    vec = A[:,0].transpose()
    housevector = vec + math.copysign(linalg.norm(vec), vec[0,0])*np.eye(1, n)
    scalarhouse = 2/ np.dot(housevector, housevector.transpose())
    H = A[:,:]
    H[0,0] = math.copysign(linalg.norm(vec), -1*vec[0,0])
    for i in range(1,m):
        H[i,0] = 0
    for z in range(1,n):
        vector = A[0:,z].transpose()
        v_ = vector - scalarhouse * np.dot(housevector, vector.transpose())*housevector
        for i in range(n):
            H[i,z] = v_[0,i]
    print(f'\033[32m{id_index}. Schritt:\033[0m\nHouseholder Vektor: \n{housevector}\nMatrix:\n{H}')
    if n > 2:
        Hh = householder_step(H[1:,1:], id_index=id_index+1)
        for i in range(1,n):
            for j in range(1,n):
                H[i,j] = Hh[i-1,j-1]
    return H
    
def householder(A):
    '''
    Householder Transformation of Matrix A.
    ----------
    Parameter:
    ----------
    A: np.matrix
        The Matrix that is to be transformed
    --------
    Returns:
    --------
    H: np.matrix
        The transformed matrix
    '''
    print(f'Starting Householder Transformation for Matrix\n{A}\n')
    H = householder_step(A)
    print(f'\033[32mErgebnis:\033[0m\n{H}')
    return H
    
    
# def householderspiegelung(M):
#   n,m = M.shape
#   vec = M[1:,0].transpose()
#   housevector = vec + math.copysign(scl.norm(vec), vec[0,0])*np.eye(1, n-1)
#   scal = 2/ np.dot(housevector, housevector.transpose())
#   M[1,0] = math.copysign(scl.norm(vec), -1*vec[0,0])
#   for i in range(2,m):
#     M[i,0] = 0
#   vecs = np.array([])
#   for z in range(1,n):
#     vector = M[1:,z].transpose()
#     vector_ = vector - scal*np.dot(housevector,vector.transpose())*housevector
#     for i in range(1,n):
#       M[i,z] = vector_[0,i-1]
#   for r in range(0,n):
#     vector = M[r,1:]
#     row = vector - scal*np.dot(vector,housevector.transpose())*housevector
#     _,l = row.shape
#     for x in range(l):
#       M[r,x+1] = row[0,x]

#   return M