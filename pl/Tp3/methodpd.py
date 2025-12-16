
PoidsObjet = [10,7,8,4]
ValeurObjet = [100,63,56,12]
Objet = [1,2,3,4]
W = 16
n = len(PoidsObjet)

B = [[0]*(W+1) for _ in range(n)]

for p in range(W+1):
    B[0][p] = 0 
    if p < PoidsObjet[0] :
        else :
            ValeurObjet[0]

for k in range(1, n):
    for p in range(W+1):
        if p < PoidsObjet[k]:
            B[k][p] = B[k-1][p]
        else:
            B[k][p] = max(B[k-1][p], B[k-1][p - PoidsObjet[k]] + ValeurObjet[k])

selection = []
k = n-1
p = W

while k >= 0 and p > 0:
    if k == 0:
        if B[k][p] > 0:
            selection.append(Objet[k])
        break
    if B[k][p] != B[k-1][p]:
        selection.append(Objet[k])
        p -= PoidsObjet[k]
    k -= 1

selection.reverse()

# Résultat
print("Objets sélectionnés:", selection)
print("Valeur maximale:", B[n-1][W])
