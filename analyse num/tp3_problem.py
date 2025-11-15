import random
import time
from tp1_problem import *
from tp2_problem import *
from p1votNonNull import Algo_trianNonNull 
from p2votPartiel import Algo_trianPartiel 
from p3vot_total import triangulation as Algo_pivot_total
from p3vot_total import remontee as Algo_remontee_total


def generate_random_system(N):
    T = [[random.randint(1, 10) for _ in range(N)] for _ in range(N)]
    B = [random.randint(1, 10) for _ in range(N)]
    return T, B


if __name__ == "__main__":

    N = int(input("Enter the size of the matrix: "))

    # Initialize global system with random values
    T, B = generate_random_system(N)
    X = [0 for i in range(N)]

    while True:
        print("\n------ MATRIX OPERATIONS MENU ------")
        print("1- Lire system.")
        print("2- afficher system.")
        print("3- Solution par methode de remontee.")
        print("4- Solution par methode de descente.")
        print("5- methode cramer.")
        print("6- Solution par pivot non null.")
        print("7- Solution par pivot partiel.")
        print("8- Solution par pivot total.")

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
        if operation == 6:
            Algo_trianNonNull(T, N, B)
            print("-----------Gauss avec pivot non nul-----------")
            print(". La matrice reduite : ")
            for i in range(N):
                print(T[i], " | ", B[i])

            X = Algo_remontee(T, N, B)
            print("\n. La solution est :")
            for i in range(len(X)):
                print(f"x[{i}] = {X[i]}")

        if operation == 7:
            Algo_trianPartiel(T, 3, B)
            print("-----------Gauss avec pivot partiel-----------")
            print(". La matrice reduite : ")
            for i in range(3):
                print(T[i], " | ", B[i])

            X = Algo_remontee(T, 3, B)
            print("\n. La solution est :")
            for i in range(len(X)):
                print(f"x[{i}] = {X[i]}")
        if operation == 8:
            print("-----------Gauss avec pivot total-----------")
            start_time = time.time()
            T_tri, B_tri, pivot_col = Algo_pivot_total(T, B)
            X = Algo_remontee_total(T_tri, B_tri, pivot_col)
            end_time = time.time()
            print("La solution est :")
            for i in range(len(X)):
                print(f"x[{i}] = {X[i]:.2f}")
            print(f"Execution time: {end_time - start_time:.6f} seconds\n")

        Global_answer = input("Continue? (Y/N): ")
        if Global_answer.strip().lower() in ["n", "no"]:
            break
