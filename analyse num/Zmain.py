import random
import time
from tp1_problem import *
from tp2_problem import *
from p1votNonNull import * 
from p2votPartiel import *
from p3vot_total import triangulation as Algo_pivot_total 
from p3vot_total import remontee as Algo_remontee_total
from p3vot_total import Algo_pivot_total_rec
from algoLU import Decomposition_LU
from algoLU import Decomposition_LU_rec
from GaussJordan import *
from GaussSeidel import *
from Jacobi import *

def generate_random_system(N):
    T = [[random.randint(1, 10) for _ in range(N)] for _ in range(N)]
    B = [random.randint(1, 10) for _ in range(N)]
    return T, B


if __name__ == "__main__":

    N = int(input("Entrer la taille de la matrice : "))

    T, B = generate_random_system(N)
    X = [0 for i in range(N)]

    while True:
        print("\n------ MATRIX OPERATIONS MENU ------")
        print("1- Lire system.")
        print("2- afficher system.")
        print("3-Methodes direct.")
        print("4- Methodes itératives")
        print("--------------------------------------\n")
        operation = int(input("Choose a number: "))
        if operation == 1:
            Lire_Systeme(T, B, N)
        if operation == 2:
            afficher_Systeme(T, B, N)
        if operation ==3:
            print("\n-- choisir la methode direct :")
            print("3.1- Crammer")
            print("3.2- Gauss-pivot non null")
            print("3.3- Gauss-pivot partial")
            print("3.4- Gauss pivot total")
            print("3.5- decomposition LU")
            print("3.6- Decomposititon Gauss-Jordan")
            operation2 = float(input("Choose a number: "))
            if operation2 == 3.1:
                while True:
                    print("\n1-Iterative")
                    print("2-Recursive\n")
                    operationcram = int(input("Choose a number: "))
                    if operationcram == 1:
                    
                        X = method_cramer(T, N, B)
                    if operationcram == 2:
                        X = method_cramer_rec(T, N, B, 0)

                    for i in range(N):
                        print("x[%d] = %.2f" % (i, X[i]))
                    answer = input("Continue dans Crammer? (Y/N): ")
                    if answer.strip().lower() in ["n", "no"]:
                        break

                    
            if operation2 == 3.2:
                while True:
                    print("\n1-Iterative")
                    print("2-Recursive\n")
                    operationnonull = int(input("Choose a number: "))
                    if operationnonull == 1:               
                        X = Algo_trianNonNull(T, N,B)
                        X = Algo_remontee(T, N, B)
                        print("la solution est: ")  
                        for i in range(N):
                            print("x[%d] = %.2f" % (i, X[i]))
                    if operationnonull == 2:
                        Algo_trianNonNull_rec(T, B, N, 0)
                        X = Algo_remontee_rec(T, N, B, 0)
                        print("la solution est: ")  
                        for i in range(N):
                            print("x[%d] = %.2f" % (i, X[i]))
                    answer = input("\nContinue dans pivot non null? (Y/N): ")
                    if answer.strip().lower() in ["n", "no"]:
                        break


                    


            if operation2 == 3.3:
                while True:
                    print("\n 1- Iterative")
                    print("2- Recursive\n")
                    operationpartiel = int(input("Choose a number: "))
                    if operationpartiel ==1:  
                        X = Algo_trianPartiel(T, N,B)
                        X = Algo_remontee(T, N, B)
                        print("la solution est: ")  
                        for i in range(N):
                            print("x[%d] = %.2f" % (i, X[i]))
                    if operationpartiel ==2:
                        Algo_trianPartiel_rec(T, B, N, 0)
                        X = Algo_remontee_rec(T, N, B, 0)
                        print("la solution est: ")  
                        for i in range(N):
                            print("x[%d] = %.2f" % (i, X[i]))
                    answer = input("\nContinue dans pivot partiel? (Y/N): ")
                    if answer.strip().lower() in ["n", "no"]:
                        break


                    


            if operation2 == 3.4:
                while True:
                    print("\n 1- Iterative")
                    print("2- Recursive\n")
                    operationtotal = int(input("Choose a number: "))


                    if operationtotal ==1:                        
                        T_tri, B_tri, pivot_col = Algo_pivot_total(T, B)
                        X = Algo_remontee_total(T_tri, B_tri, pivot_col)
                        print("La solution est :")
                        for i in range(len(X)):
                            print(f"x[{i}] = {X[i]:.2f}")


                    if operationtotal ==2:
                        T, B, perm = Algo_pivot_total_rec(T, B, N,0)
                        X = Algo_remontee_total(T, N, B, perm)
                        print("la solution est: ")
                        for i in range(N):
                             print("x[%d] = %.2f" % (i, X[i]))
                    answer = input("\nContinue dans pivot total? (Y/N): ")
                    if answer.strip().lower() in ["n", "no"]:
                        break

                    


   
            if operation2 == 3.5:
                    while True:
                        print("\n 1- Iterative")
                        print("2- Recursive\n")
                        operationLU = int(input("Choose a number: "))
                        if operationLU ==1:
                            start_time = time.time()

                            print("\nDécomposition LU itérative:")
                            L, U = Decomposition_LU(T, N)
                            print("Matrice L:")
                            for row in L:
                                print(row)
                            print("Matrice U:")
                            for row in U:
                                print(row)

                            X = Algo_descente(L,N,B)
                            solution= Algo_remontee(U,N,X)
                            for i in range (N):
                                print("x[%d] = %f" % (i, solution[i]))
                            end_time = time.time()
                            print(f"Temps d'exécution: {end_time - start_time:.6f} s")
                        if operationLU ==2:
                            print("\nDécomposition LU recursive:")
                            start_time = time.time()
                            L, U = Decomposition_LU_rec(T, N)
                            print("Matrice L:")
                            for row in L:
                                print(row)
                            print("Matrice U:")
                            for row in U:
                                print(row)

                            X = Algo_descente(L,N,B)
                            solution= Algo_remontee(U,N,X)
                            for i in range (N):
                                print("x[%d] = %f" % (i, solution[i]))
                            end_time = time.time()
                            print(f"Temps d'exécution: {end_time - start_time:.6f} s\n")
                        answer = input("\nContinue dans LU? (Y/N): ")
                        if answer.strip().lower() in ["n", "no"]:
                            break
            if operation2 == 3.6:
                while True:
                    print("\n 1- Iterative.")      
                    print("2-Recursive.\n")  
                    operationGauss = int(input("Choose a number: "))       
                    if operationGauss==1: 
                        time_start = time.time() 
                                              
                        X = Gauss_jordan(T, B)
                        print("La solution est :")
                        for i in range(len(X)):
                            print(f"x[{i}] = {X[i]:.2f}")
                        time_end = time.time()
                        print(f"Execution time: {time_end - time_start:.6f} s\n")

                    if operationGauss==2:
                        start_time = time.time()
                        A = former_aug(T,B)
                        X = Gauss_jordan_rec(A, B, N)

                        print("La solution est :")
                        for i in range(len(X)):
                            print(f"x[{i}] = {X[i]:.2f}")
                        end_time = time.time()
                        print(f"Execution time: {end_time - start_time:.6f} s\n")


                    answer = input("\nContinue dans Gauss-Jordan? (Y/N): ")
                    if answer.strip().lower() in ["n", "no"]:
                        break


        if operation ==4:
            print("\n-- choisir la methode itérative :")
            print("4.1- Jacobi")
            print("4.2- Gauss-Seidel\n")
            operation2 = float(input("Choose a number: "))
            if operation2 == 4.1:
                while True:
                    print("1- iterative")
                    print("2- recursive\n")
                    operationJacobi = int(input("Choose a number: "))
                    if operationJacobi ==1:
                         time_start = time.time()
                         N_max = int(input("Entrer le nombre d'itérations maximales : "))
                         X = Jacobi(T, B, N_max)
                         time_end = time.time()
                         print(f"Execution time: {time_end - time_start:.6f} seconds\n")
                    if operationJacobi ==2:
                         time_start = time.time()
                         N_max = int(input("Entrer le nombre d'itérations maximales : "))
                         X = Jacobi_rec(T, B, N_max, None,0)
                         time_end = time.time()  
                         print(f"Execution time: {time_end - time_start:.6f} seconds\n")
                 
                    answer = input("\nContinue dans Jacobi? (Y/N): ")
                    if answer.strip().lower() in ["n", "no"]:
                        break

                  
            if operation2 == 4.2:
                while True:
                    print("\n1- iterative")
                    print("2- recursive\n")
                    operationGaussSeidel = int(input("Choose a number: "))
                    if operationGaussSeidel ==1:
                         time_start = time.time()
                         N_max = int(input("Entrer le nombre d'itérations maximales : "))
                         X = Gauss_Seidel(T, B, N_max)
                         time_end = time.time()
                         print(f"Execution time: {time_end - time_start:.6f} seconds\n")
                    if operationGaussSeidel ==2:
                            time_start = time.time()
                            N_max = int(input("Entrer le nombre d'itérations maximales : "))
                            X = Gauss_Seidel_rec(T, B, N_max, None,0)
                            time_end = time.time()
                            print(f"Execution time: {time_end - time_start:.6f} seconds\n")


                    answer = input("\nContinue dans Gauss Seidel? (Y/N): ")
                    if answer.strip().lower() in ["n", "no"]:
                        break

                        

        Global_answer = input("\nContinue au Menu ? (Y/N): ")
        if Global_answer.strip().lower() in ["n", "no"]:
            break
