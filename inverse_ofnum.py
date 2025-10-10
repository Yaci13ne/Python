import math
N =  int (input("Enter a number N : "))
num_digit = int(math.log10(N))+1

i = num_digit - 1
print (i)
print (num_digit)

dup = N
result = 0
while (dup>0) :
  result = result + (dup%10)*(10**i)
  dup = dup//10
  i-=1

print("the inverse of %d is %d"%(N,result ))



