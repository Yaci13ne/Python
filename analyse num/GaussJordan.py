from display_matricaug import former_aug
import time
def Gauss_jordan(A, B):
    
    N = len(A)
    X = [0]*N
    A = former_aug(A, B)   
    for k in range(N):

        pivot = A[k][k]

        for j in range(N+1):
            A[k][j] /= pivot

        for i in range(N):
            if i != k:
                q = A[i][k]
                for j in range(k, N+1):
                    A[i][j] -= (q) * A[k][j]

    for i in range(N):
        X[i] = A[i][N]

    return X


def Gauss_jordan_rec(A, B, N, k=0):
    if k >= N:
        X = [0]*N
        for i in range(N):
            X[i] = A[i][N]
        return X

    pivot = A[k][k]

    for j in range(N + 1):
        A[k][j] /= pivot

    for i in range(N):
        if i != k:
            q = A[i][k]
            for j in range(k, N + 1):
                A[i][j] -= q * A[k][j]

    return Gauss_jordan_rec(A, B, N, k + 1)


if __name__ == "__main__":
    print("-----Gauss-Jordan-----")

    A = [[2, 1, -1],
         [-3, -1, 2],
         [-2, 1, 2]]

    B = [8, -11, -3]

    X = Gauss_jordan(A, B)
    print("La solution est :")
    for i in range(len(X)):
        print(f"x[{i}] = {X[i]:.2f}")
