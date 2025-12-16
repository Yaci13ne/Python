# article, poids, valeur
T = [[1,10,100],[2,7,63],[3,8,56],[4,4,12]]

#minimum poids
def poids(article):
    return article[1]
    



def glouton(T, W):
    T.sort(key=poids)

    poids_total = 0
    selection = []
    for article in T:
        if  article[1] <= W:
            poids_total += article[1]
            W -= article[1]
            selection.append(article[0])

    return selection, poids_total   
    


W = 16
selection, poids_total = glouton(T, W)
print("Reponse est :")
print("Articles selectionnes:", selection
      )
print("Poids total:", poids_total)
