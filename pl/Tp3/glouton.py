# article, poids, valeur
T = [[1,10,100],[2,7,63],[3,8,56],[4,4,12]]
#maximum value 
def value(article):
    return article[2]   

def glouton(T, W):
    T.sort(key=value, reverse=True)

    poids_total = 0
    valeur_totale = 0
    selection = []

    for article in T:
        if poids_total + article[1] <= W:
            selection.append(article[0])
            poids_total += article[1]
            valeur_totale += article[2]

    return selection, poids_total, valeur_totale


W = 16
selection, poids_total, valeur_totale = glouton(T, W)
print("Reponse est :")
print("Articles selectionnes:", selection
      )
print("Poids total:", poids_total)
print("valeur totale  :",valeur_totale)