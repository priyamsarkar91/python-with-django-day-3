a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
find_max = lambda a, b: max(a, b)

result = find_max(a,b)
print("max of",a,"and",b,"is",result)
