sexe = input("Entrer le sexe (la reponse est avec homme /femme) : ")
age = int(input("Entrer l'age: "))

if (sexe =="homme" and age>20) or (sexe == "femme" and 18<age<35) :
  print ("il faut que tu pais. ")

else :
   print (" tu ne pais pas. ")