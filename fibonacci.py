
def fibonacci (n):
    if(n<=1) : return n
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(7))
print("The first 10 elements : ")
for i in range (0,10):
    print(fibonacci(i),end=' ')