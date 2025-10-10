def multiplication (N):
  for i in range (1,10+1):
    print("%d * %d = %d" %(N,i,N*i))



while True :
  N = int(input("Enter N to calculate its multiplication table: "))
  if(N>0):
    break

multiplication(N)