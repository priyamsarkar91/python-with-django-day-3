def mul(n):
    if(n==1):
        return 1
    else:
        return n*mul(n-1)
    
a = int(input("Enter a  integer: "))
result = mul(a)
print("mul of",a,"=",result)