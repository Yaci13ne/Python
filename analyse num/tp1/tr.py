print("Resolution de l'Equation du Premier Degre aX + b = 0")
print("Entrez les coefficients a et b")
a=float(input("a = "))
b=float(input("b = "))
if (a==0 and b==0):
   print("X possède une infinité de solutions dans R")
elif (a==0 and b!=0):
    print ("X ne possède pas de solution dans R")
elif (a!=0 and b==0):
       print("X=0 est la solution unique dans R")
else:
            print("X=",-b/a,"est la solution dans R")