#Calculer la somme des carres de n premiers nombres impairs 
import math
while True : 
    n = int(input("Enter a number :"))
    if n>=0:
     break

i = 1
counter = 0
result =0
while counter<n:
 result = i**2 + result
 i+=2
 counter+=1


print(result)