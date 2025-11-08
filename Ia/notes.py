def analyse_liste(liste) :
    positives = [x for x in liste if x >= 0]

    return f'the min : {min(liste)}, the max : {max(liste)}, the moyen : {(sum(liste)/len(liste)):.2f}, positives : {positives}'
      




print(analyse_liste([11,12.5,3,14,12,6.5,10]))