def multiply(a,b):

    if a < b:
        return product(b,a)#if  is less than b swap the numbers
    elif b != 0:
        return a + multiply(a,b-1)#calculate b times sum of a
    else:
        return 0 #if any of the two numbers is zero then return zero


a=5
b=2
print(multiply(a,b))

