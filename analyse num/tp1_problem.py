import random


def Read_matrix(T, N):

    print("Enter the values of the matrix:")
    for i in range(N):
        for j in range(N):
            print("T[%d][%d] = " % (i, j), end=" ")
            T[i][j] = int(input())


def Disp_matrix(T, N):
    for i in range(N):
        print()
        for j in range(N):
            print(T[i][j], end=" ")
        print()


def initial_matrix():
    N = random.randint(1, 3)
    T = [[0 for j in range(N)] for i in range(N)]

    for i in range(N):
        for j in range(N):
            T[i][j] = random.randint(0, 10)

    print("This is the matrix:")
    Disp_matrix(T, N)
    return T


def Mat_identite(N):
    id = [[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                id[i][j] = 1
    print("Identity matrix:")
    Disp_matrix(id, N)
    return id


def Sum_Matrices(T, T2, N):
    s = [[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            s[i][j] = T[i][j] + T2[i][j]
    print("Sum of the two matrices:")
    Disp_matrix(s, N)


def Prod_Matrices(T, T2, N):
    prod = [[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                prod[i][j] += T[i][k] * T2[k][j]
    print("\nProduct of the matrices:")
    Disp_matrix(prod, N)


def Transp_Matrice(T, N):
    transp = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            transp[i][j] = T[j][i]
    print("Transpose of the matrix:")
    Disp_matrix(transp, N)


def TriangulaireSup_Matrice(T, N):
    for i in range(N):
        for j in range(N):
            if j < i and T[i][j] != 0:
                return False

    return True


def TriangulaireInf_Matrice(T, N):
    for i in range(N):
        for j in range(N):
            if j > i and T[i][j] != 0:
                return False

    return True


def Diagonal(T, N):
    flag = 0
    for i in range(N):
        for j in range(N):
            if i != j and T[i][j] != 0:
                flag = 1
                print("The matrix is not diagonal.")
                break
        if flag == 1:
            break
    if flag == 0:
        print("The matrix is diagonal.")


def Symmetric(T, N):
    flag = 0
    for i in range(N):
        for j in range(N):
            if T[i][j] != T[j][i]:
                flag = 1
                print("The matrix is not symmetric.")
                break
        if flag == 1:
            break
    if flag == 0:
        print("The matrix is symmetric.")


def Diagonal(T, N):
    det = 1
    for i in range(N):
        det *= T[i][i]
    return det


"""
def Determinant(T, N):
    if all(T[i][j] == (1 if i == j else 0) for i in range(N) for j in range(N)):
        return 1

    is_upper = TriangulaireSup_Matrice(T, N)
    is_lower = TriangulaireInf_Matrice(T, N)

    if is_upper or is_lower:
        det =Diagonal
        return det

    if N == 1:
        return T[0][0]

    if N == 2:
        return T[0][0] * T[1][1] - T[0][1] * T[1][0]

    if N == 3:
        return (
            T[0][0] * (T[1][1] * T[2][2] - T[1][2] * T[2][1])
            - T[0][1] * (T[1][0] * T[2][2] - T[1][2] * T[2][0])
            + T[0][2] * (T[1][0] * T[2][1] - T[1][1] * T[2][0])
        )

"""


def Determinant(T, N):
    if N == 1:
        return T[0][0]

    is_upper = TriangulaireSup_Matrice(T, N)
    is_lower = TriangulaireInf_Matrice(T, N)

    if is_upper or is_lower:
        det = 1
        for i in range(N):
            det *= T[i][i]
        return det

    det = 0
    sign = 1

    for i in range(N):
        submatrix = []
        for j in range(1, N):
            row = []
            for k in range(N):
                if k != i:
                    row.append(T[j][k])
            submatrix.append(row)

        det += sign * T[0][i] * Determinant(submatrix, N - 1)
        sign = -sign

    return det


def SwapRows(T, N, row1, row2):

    r1 = row1 - 1
    r2 = row2 - 1
    i = 0
    if N >= 2:
        while i < N:
            T[r1][i], T[r2][i] = T[r2][i], T[r1][i]
            i += 1


def SwapColumns(T, N, col1, col2):
    c1 = col1 - 1
    c2 = col2 - 1
    i = 0
    if N >= 2:
        while i < N:
            T[i][c1], T[i][c2] = T[i][c2], T[i][c1]
            i += 1

if __name__ == "__main__":
 while True:
     print("1 - Use an initial random matrix")
     print("2 - Create your own matrix")
 
     choose = int(input("Choose a number: "))
     print()
     if choose == 1 or choose == 2:
         break
 
 if choose == 1:
     T = initial_matrix()
     N = len(T)
     while True:
         print("\n------ MATRIX OPERATIONS MENU ------")
 
         print("1 - Calculate its transpose")
         print("2 - Test if it is upper triangular")
         print("3 - Test if it is lower triangular")
         print("4 - Test if it is diagonal")
         print("5 - Test if it is symmetric")
         print("6 - Display its identity matrix")
         print("7 - Calculate the determinant")
         print("8 - Swap between Rows")
         print("9 - Swap between Columns")

         operation1 = int(input("Choose a number: "))
         if operation1 == 1:
             Transp_Matrice(T, N)
         if operation1 == 2:
             if TriangulaireSup_Matrice(T, N):
                 print("The matrix is Upper triangular")
             else:
                 print("The matrix is not Upper triangular")

         if operation1 == 3:
             if TriangulaireInf_Matrice(T, N):
                 print("The matrix is Lower triangular")
             else:
                 print("The matrix is not Lower triangular")
         if operation1 == 4:
            Diagonal(T, N)
         if operation1 == 5:
             Symmetric(T, N)
         if operation1 == 6:
             Mat_identite(N)
         if operation1 == 7:
             det = Determinant(T, N)
             print("The determinant is : ", det)
         if operation1 == 8:
             if N == 1:
                 print("Can't swap if it is just one number 1*1")
             else:
                 r1 = int(input("Enter the first row: "))
                 r2 = int(input("Enter the second row: "))
                 SwapRows(T, N, r1, r2)
                 Disp_matrix(T, N)
         if operation1 == 9:
             if N == 1:
                 print("Can't swap if it is just one number 1*1")

             else:
                 c1 = int(input("Enter the first column: "))
                 c2 = int(input("Enter the second column: "))
                 SwapColumns(T, N, c1, c2)
                 Disp_matrix(T, N)

         answer = input("Continue? (Y/N): ")
         if answer.strip().lower() in ["n", "no"]:
             break

 if choose == 2:
     while True:
         N = int(input("Enter N (the size of the matrix): "))
         if N > 0:
             break
     T = [[0 for j in range(N)] for i in range(N)]
 
     T2 = [[0 for j in range(N)] for i in range(N)]
     Read_matrix(T, N)

     while True:
         print("1 - Display it")
         print("2 - Display its identity matrix")
         print("3 - Add a second matrix and calculate their sum")
         print("4 - Add a second matrix and calculate their product")
         print("5 - Test if it is upper triangular")
         print("6 - Test if it is lower triangular")
         print("7 - Test if it is diagonal")
         print("8 - Test if it is symmetric")
         print("9 - Calculate the determinant")
         print("10 - Swap between Rows")
         print("11- Swap between Columns")
         operation2 = int(input("Choose a number: "))

         if operation2 == 1:
             Disp_matrix(T, N)
         if operation2 == 2:
             Mat_identite(N)
         if operation2 == 3:
             Read_matrix(T2, N)
             Sum_Matrices(T, T2, N)
         if operation2 == 4:
            Read_matrix(T2, N)
            Prod_Matrices(T, T2, N)
         if operation2 == 5:
            TriangulaireSup_Matrice(T, N)
         if operation2 == 6:
            TriangulaireInf_Matrice(T, N)
         if operation2 == 7:
            Diagonal(T, N)
         if operation2 == 9:
            det = Determinant(T, N)
            print("The determinant is : ", det)
         if operation2 == 10:
            r1 = int(input("Enter the first row: "))
            r2 = int(input("Enter the second row: "))
            SwapRows(T, N, r1, r2)
            Disp_matrix(T, N)

         if operation2 == 11:
            c1 = int(input("Enter the first column: "))
            c2 = int(input("Enter the second column: "))
            SwapColumns(T, N, c1, c2)
            Disp_matrix(T, N)
 
         answer = input("Continue? (Y/N): ")
         if answer.strip().lower() in ["n", "no"]:
            break

