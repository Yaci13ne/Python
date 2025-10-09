import math
while True :
  N= int(input("Enter a number : "))
  if N>=0:
    break

flag = 1
for i in range (2,int(math.sqrt(N)+1)) :
  if (N%2==0):
    print("ce nombre n'est pas premier")
    flag =0
    break

if flag==1 :
  print("Ce %d est un nombre premier "%N)