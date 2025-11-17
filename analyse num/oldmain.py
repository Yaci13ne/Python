from tp1_problem import *
from tp2_problem import *
from fct_elimination import fct_elimination


if __name__ == "__main__":

    N = int(input("Enter the size of the matrix: "))
    T = [[0 for i in range(N)] for j in range(N)]
    B = [0 for i in range(N)]
    X = [0 for i in range(N)]

    while True:
        print("\n------ MATRIX OPERATIONS MENU ------")
        print("1- Lire system.")
        print("2- afficher system.")
        print("3- methode de remontee.")
        print("4- methode de descente.")
        print("5- methode cramer.")
        operation = int(input("Choose a number: "))
        if operation == 1:
            Lire_Systeme(T, B, N)
        if operation == 2:
            afficher_Systeme(T, B, N)
        if operation == 3:
            while True:
                print("1- remontee iterative. ")
                print("2- remontee recursive. ")
                operationrem = int(input("Choose a number: "))
                if operationrem == 1:
                    X = Algo_remontee(T, N, B)
                if operationrem == 2:
                    X = Algo_remontee_rec(T, N, B, 0)

                print("la solution est: ")
                for i in range(N):
                    print("x[%d] = %f" % (i, X[i]))

                answer = input("autre fois (Y/N): ")
                if answer.strip().lower() in ["n", "no"]:
                    break

        if operation == 4:
            while True:
                print("1- descent iterative. ")
                print("2- descent recursive. ")
                operationdesc = int(input("Choose a number: "))
                if operationdesc == 1:
                    Algo_descente(T, N, B)
                if operationdesc == 2:
                    Algo_descente_rec(T, N, B)

                print("la solution est: ")
                for i in range(N):
                    print("x[%d] = %f" % (i, X[i]))
                answer = input("autre fois (Y/N): ")
                if answer.strip().lower() in ["n", "no"]:
                    break
        if operation == 5:
            while True:
                print("1- Cramer iterative. ")
                print("2- Cramer recursive. ")
                operationcram = int(input("Choose a number: "))
                if operationcram == 1:
                    X = method_cramer(T, N, B)
                if operationcram == 2:
                    X = method_cramer_rec(T, N, B, 0)

                print("la solution est: ")
                for i in range(N):
                    print("x[%d] = %f" % (i, X[i]))
                answer = input("autre fois (Y/N): ")
                if answer.strip().lower() in ["n", "no"]:
                    break
        Global_answer = input("Continue? (Y/N): ")
        if Global_answer.strip().lower() in ["n", "no"]:
            break
