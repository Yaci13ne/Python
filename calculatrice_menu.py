while True :
  print("1 - Addition")
  print("2 - Subtraction")
  print("3 - division")
  print("4 - multiplication")
  operation = int(input("Choose the number of calcul you wanna do ?"))
  print()
  A = int (input("Enter A : "))
  B = int (input("Enter B : "))
  
  if operation == 1 :
      print ("the result is :",A+B)
  elif operation == 2 :
    print ("the result is :",A-B)
  elif operation == 3 :
    if B!=0 :
      print ("the result is :",A/B)
    else : 
      print("Impossible B = 0")
  elif operation == 4 :
    print ("the result is :",A*B)
  

  answer = input("Do you want to continue (Y/N) ?")
  if answer == 'N' :
    break


