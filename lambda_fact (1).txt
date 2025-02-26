a= int(input("enter the number:"))
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
result= factorial(a)
print("factorial of",a,"=",result)