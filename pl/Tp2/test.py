# Import de la bibliothèque numpy pour les calculs matriciels
import numpy as np

def saisir_matrice():
    # Coefficients de la fonction objectif (maximiser z = 800x1 + 300x2)
    Cj = np.array([800, 300, 0, 0, 0])
    
    # Variables de base initiales (les variables de surplus S1, S2, S3)
    VB = ['S1', 'S2', 'S3']
    
    # Tableau initial (colonnes: b, x1, x2, S1, S2, S3)
    # Chaque ligne représente une contrainte
    tableau = np.array([
        [400, 2, 1, 1, 0, 0],   # 2x1 + x2 + S1 = 400
        [150, 1, 0, 0, 1, 0],   # x1 + S2 = 150
        [200, 0, 1, 0, 0, 1]    # x2 + S3 = 200
    ], dtype=float)
    
    return Cj, VB, tableau

def calculer_Cj_moins_Zj(Cj, VB, tableau):
    n = len(Cj)
    m = len(tableau)
    
    Zj = np.zeros(n)
    for j in range(n):
        somme = 0
        for i in range(m):
            index = ['x1', 'x2', 'S1', 'S2', 'S3'].index(VB[i])
            somme += Cj[index] * tableau[i, j+1]
        Zj[j] = somme
    
    return Cj - Zj

def choisir_variable_entrante(Cj_moins_Zj):
    max_val = np.max(Cj_moins_Zj)
    if max_val <= 0:
        return -1  
    return np.argmax(Cj_moins_Zj)

def choisir_variable_sortante(tableau, var_entrant_index):
    # Calcule les ratios b / coefficient colonne variable entrante
    ratios = []
    for i in range(len(tableau)):
        coeff = tableau[i, var_entrant_index + 1]
        if coeff > 0:
            ratios.append(tableau[i, 0] / coeff)
        else:
            ratios.append(np.inf)
    min_ratio = np.min(ratios)
    if min_ratio == np.inf:
        return -1  # Solution non bornée
    return np.argmin(ratios)

def pivot(tableau, var_entrant_index, var_sortant_index):
    pivot_element = tableau[var_sortant_index, var_entrant_index + 1]
    # Diviser la ligne pivot par l'élément pivot
    tableau[var_sortant_index, :] /= pivot_element
    
    # Mettre à jour les autres lignes pour obtenir des 0 dans la colonne pivot
    for i in range(len(tableau)):
        if i != var_sortant_index:
            facteur = tableau[i, var_entrant_index + 1]
            tableau[i, :] -= facteur * tableau[var_sortant_index, :]

def methode_simplexe():
    Cj, VB, tableau = saisir_matrice()
    print("Tableau initial:")
    print(tableau)
    print("Variables de base:", VB)
    
    while True:
        Cj_moins_Zj = calculer_Cj_moins_Zj(Cj, VB, tableau)
        print("\nCj - Zj:", Cj_moins_Zj)
        
        var_entrant = choisir_variable_entrante(Cj_moins_Zj)
        if var_entrant == -1:
            print("Solution optimale trouvée!")
            break
        
        print("Variable entrante colonne:", var_entrant)
        
        var_sortant = choisir_variable_sortante(tableau, var_entrant)
        if var_sortant == -1:
            print("Solution non bornée.")
            break
        
        print("Variable sortante ligne:", var_sortant)
        pivot(tableau, var_entrant, var_sortant)
        
        # Mise à jour de la variable de base
        VB[var_sortant] = ['x1', 'x2', 'S1', 'S2', 'S3'][var_entrant]
        
        print("Tableau après pivot:")
        print(tableau)
        print("Variables de base:", VB)
    
    print("\nTableau final:")
    print(tableau)

# Lancer la méthode simplexe
methode_simplexe()





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
        slack = [0] * m
        slack[i] = 1
        ligne.extend(slack)
        tableau.append(ligne)

    tableau = np.array(tableau, dtype=float)
    return Cj, VB, tableau

def display_tableau(Cj, VB, tableau):   
    header = ["b"] + [f"x{j+1}" for j in range(len(Cj)-len(VB))] + VB
    print("\nTableau actuel:")
    print(" | ".join(f"{h:>8}" for h in header))
    for i, row in enumerate(tableau):
        print(" | ".join(f"{val:8.2f}" for val in row))
    print()

# Test
Cj, VB, tableau = saisir_matrice()
display_tableau(Cj, VB, tableau)
