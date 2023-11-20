def Recursion(n): #calculating factorial using recursion
    if n==0:
        return 1
    else:
        return (n*Recursion(n-1))

def Iteration(n): #calculating factorial using Iteration
    fact = 1;

    for i in range(1,n+1):
        fact*= i

    return fact


print(Recursion(5))
print(Iteration(5))

     
