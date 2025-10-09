#Un magasin facture 0,30 dh les dix premières photocopies, 0,25 dh les vingt suivantes et 0,20 dh au-delà. Ecrire un programme qui demande à l’utilisateur le nombre de photocopies effectuées et qui affiche la facture correspondante.

N = int (input('Enter N number of photocopies : '))

if N<=10 :
  prix = N* 0.3
elif N>10 & N<=30 : 
    prix = 10*0.3 + (N-10)*0.25
  
elif N>30:
    prix = 10*0.3 + 20*0.25 +(N-30)*0.20


print('the price is %.2f dh' %prix)
