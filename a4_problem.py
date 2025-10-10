#l'ordinateur tire un nombre au hasard entre 1 et 30 et vous avez cinq essais pour le trouver. Après chaque tentative, l'ordinateur vous dira si le nombre que vous avez proposé est trop grand, trop petit, ou si vous avez trouvé le bon nombre.


import random
pc_number = random.randint(1,30)
i = 1
print ("you have 5 tries to guess which number the pc choosed :")

while True :

  user_number = int(input("(%d' try): "%i))
  if user_number == pc_number :
    print("You won!!Congratsss")
    break
  else :
    i+=1
  if(i>5) :
    break

print ("The pc has choosed %d"%pc_number)


  


