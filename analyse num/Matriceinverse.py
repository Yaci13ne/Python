from tp1_problem import *
from display_matricaug import *
def matrice_inverse(A,N):
    I = Mat_identite
    A = former_aug(A,I)
    for k in range (N):
        pivot = A[k][k]
        for j in range (2*N):
            A[k][j] /= pivot
        for i in range (N):
            if i != k:
                q = A[i][k]
                for j in range (2*N):
                    A[i][j] -= (q) * A[k][j]






