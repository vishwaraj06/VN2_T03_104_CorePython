#Function categories
''''''
'''
1. Function with parameters, with return type
2. Function with parameters, without return type
3. Function without parameters, with return type
4. Function without parameters, without return type'''''


print("Function with parameters ,with return type")
def function(name):
    return name
print("Hi",function("gowtham"))
'''
print("******************************************")
def operation(n1,n2,n3):
    mul=n1*n2*n3
    return mul
n1=int(input("Enter n1:"))
n2=int(input("Enter n2:"))
n3=int(input("Enter n3:"))
print("Mul Operations:",operation(n1,n2,n3))'''

print("Function with parameters, without return type")

def operation(n1,n2,n3):
    mul = n1 * n2 * n3
    print("multiplication:",mul)
operation(12,34,67)
operation(n1=11,n2=11,n3=12)

print("Function without parameters, with return type")
def add():
    a=12
    b=15
    c=a+b
    return c
print("addtion is :",add())

print("Function without parameters, without return type")
def add():
    a=34
    b=45
    c=a+b
    print("Value of c:",add())
add()
print("Addition:",add())
