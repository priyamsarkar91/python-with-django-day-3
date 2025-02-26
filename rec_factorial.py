def factorial(n):
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)
    
a = int(input("Enter a  integer: "))
result = factorial(a)
print("factorial of",a,"=",result)