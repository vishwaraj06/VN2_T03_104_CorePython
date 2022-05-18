a=12
b=20
#Arithmetic operatos#
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(b//a)
print(a**b)

#Comparision operators#(TRUE oR FALSE)
a==b
print(a==b)
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)
print(a!=b)

#Assignment operators#
a=10
b=12
c=a+b
print(c)
c+=a # same as c=c+a
print(c)
c-=a # same as c=c-a
print(c)
c*=a #same as c=c*a
print(c)
c/=a # same as c=c/a
print(c)
c**=a # same as c=c**a
print(c)
c//=a # same as c=c//a
print(c)
c%=a # same as c=c%a
print(c)

# membership operators

mem_a="hello how are you" #String
mem_b=[12,'Hi',29,"bye"] # list
mem_c=(12,13,14,15,)  #tuples
print('hello' in mem_a)
print(12 in mem_b)
print(19 in mem_c)
print('hello' not in mem_a)
print(12 not in mem_b)
print(15 not in mem_c)

#python identity operators


m=int(input("Enter m:"))
n=int(input("Enter n:"))
if (m==n):
    print("m and n are same")
else:
    print("m and n are different")

