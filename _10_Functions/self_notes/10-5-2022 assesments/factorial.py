a=int(input("Enter Number:"))
def fact(a):
    fact=1
    while(a!=0):
        fact*=a
        fact=fact*a
        a=a-1
    return fact
print("factorial is",fact(a))