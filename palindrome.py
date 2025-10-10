import math

def inverse_num(N):
    num_digit = int(math.log10(N)) + 1
    i = num_digit - 1
    print("i =", i)
    print("num_digit =", num_digit)

    dup = N
    result = 0
    while dup > 0:
        result = result + (dup % 10) * (10 ** i)
        dup = dup // 10
        i -= 1
    return result

N = int(input("Enter the value of N :"))
inverse = inverse_num(N)
if (inverse == N )  :
    print("this number is palindrome ")
  
else :
    print("it is not palindrome ")


