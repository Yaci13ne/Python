while True : 
    n = int(input("Enter a number :"))
    if n>=0:
     break
fact =n
i =n-1
while i>0 :
   fact = (fact*i)   
   i=i-1

print("factorial: ",fact)