import numpy as np

def saisir_matrice():
    n = int(input("Entrer le nombre de variables de décision (ex: 2): "))
    m = int(input("Entrer le nombre de contraintes (ex: 3): "))

    VB = [f"S{i+1}" for i in range(m)]

    print("\n=== Entrée des coefficients de la fonction objectif ===")
    Cj = [float(input(f"Coefficient de x{j+1}: ")) for j in range(n)]
    Cj += [0] * m 
    Cj = np.array(Cj)

    print("\n=== Entrée des contraintes ===")
    tableau = []
    for i in range(m):
        print(f"\n→ Contrainte {i+1}:")
        b = float(input(f"Valeur du 1er membre (b{i+1}): "))
        ligne = [b]
        for j in range(n):
            a = float(input(f"Coefficient de x{j+1}: "))
            ligne.append(a)
        slack = [0]*m
        slack[i] = 1
        ligne.extend(slack)
        tableau.append(ligne)

    tableau = np.array(tableau, dtype=float)
    return Cj, VB, tableau

def display_tableau(Cj, VB, tableau):
    header = ["b"] + [f"x{j+1}" for j in range(len(Cj)-len(VB))] + VB
    print("\nTableau actuel:")
    print(" | ".join(f"{h:>8}" for h in header))
    for row in tableau:
        print(" | ".join(f"{val:8.2f}" for val in row))
    print()


def calculer_Cj_moins_Zj(Cj, VB, tableau):
    all_vars = [f"x{j+1}" for j in range(len(Cj)-len(VB))] + VB
    n = len(all_vars)
    m = len(VB)

    Zj = np.zeros(n)
    for j in range(n):
        for i in range(m):
            var_index = all_vars.index(VB[i])
            Zj[j] += Cj[var_index] * tableau[i][j+1]
    Cj_Zj = Cj - Zj
    return Cj_Zj


def chercher_variable(Cj_Zj):
    max_val = np.max(Cj_Zj)
    if max_val <= 0:
        return -1
    return np.argmax(Cj_Zj)


def chercher_variable_sort(tableau, var_index):
    ratios = []
    for i in range(len(tableau)):
        coeff = tableau[i, var_index + 1]
        if coeff > 0:
            ratios.append(tableau[i, 0] / coeff)
        else:
            ratios.append(np.inf)
    min_ratio = np.min(ratios)
    if min_ratio == np.inf:
        return -1
    return np.argmin(ratios)


def pivotage(T, pivot_ligne, pivot_colonne):
    pivot_value = T[pivot_ligne][pivot_colonne + 1]
    T[pivot_ligne] = [x / pivot_value for x in T[pivot_ligne]]

    for i in range(len(T)):
        if i != pivot_ligne:
            ratio = T[i][pivot_colonne + 1]
            T[i] = [T[i][j] - ratio * T[pivot_ligne][j] for j in range(len(T[0]))]
    return T


def solution_optimale(T, VB, Cj):
    solution = {}
    all_vars = [f"x{j+1}" for j in range(len(Cj)-len(VB))] + VB
    for i, var in enumerate(VB):
        solution[var] = T[i][0]
    for var in all_vars:
        if var not in solution:
            solution[var] = 0
    Z = sum(Cj[j]*solution[all_vars[j]] for j in range(len(Cj)))
    return solution, Z


# --- Programme principal ---
Cj, VB, tableau = saisir_matrice()
display_tableau(Cj, VB, tableau)

iteration = 1
while True:
    print(f"=== Itération {iteration} ===")
    Cj_moins_Zj = calculer_Cj_moins_Zj(Cj, VB, tableau)
    print("Cj - Zj:", ["{:.2f}".format(v) for v in Cj_moins_Zj])

    var_entrant = chercher_variable(Cj_moins_Zj)
    if var_entrant == -1:
        print("\n Solution optimale trouvée!")
        break

    print("→ Variable entrante:", f"x{var_entrant+1}")
    var_sortant = chercher_variable_sort(tableau, var_entrant)
    if var_sortant == -1:
        print("\n  Solution non bornée.")
        break

    print("→ Variable sortante:", VB[var_sortant])
    VB[var_sortant] = f"x{var_entrant+1}"
    tableau = pivotage(tableau, var_sortant, var_entrant)
    display_tableau(Cj, VB, tableau)
    iteration += 1

solution, Z = solution_optimale(tableau, VB, Cj)
print("\n=== Résultat final ===")
for var, val in solution.items():
    print(f"{var} = {val:.2f}")
print(f"\nValeur optimale de Z = {Z:.2f}")
