def manipuler_liste(liste): 
   motfin = input("Entrez un mot pour ajouter a la fin: ")
   liste.append(motfin)
   motdibut = input("Entrez un mot pour ajouter au debut: ")
   liste.insert(0, motdibut)
   print('la liste apres ajout : ', liste)
   del(liste[int(input("Entrez l'index du mot a supprimer: "))-1])
   print('la liste apres suppression : ', liste)
   
   print('trier la liste en ordre alphabetique : ', sorted(liste))
   liste.reverse()  
   print('la liste en ordre inverse : ', liste)
   print("l element supprime :")
   for i in range(0,len(liste)):
      print(liste[len(liste)-1-i],end=' ')
      liste.pop()
      if len(liste)==2: break


   return liste
   

print('\n La liste apres la manipulation',manipuler_liste(['aaaa', 'dddds', 'cccc', 'bbbb']))