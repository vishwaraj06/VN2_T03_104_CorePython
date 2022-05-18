'''a='hello'
for i in a:
    print(i.upper(),end='')'''
'''a=[1,2,3,4,5,6,7,8,9]
num=int(input("Enter:"))
for i in a:
    c=num*i
    print(c)'''
'''list=[1,2,3,4,5,6,7,8,9]
sum=0
for i in list:
    sum=sum+i

    print(sum,end='  ')'''
'''list = [10,30,23,43,65,12]
sum = 0
for i in list:
    sum = sum+i
print(sum)
a=[1,2,3,4,5,6]
for i in a:
    print(i)
list=[1,2,3,4,5,6,7,8]
mul=3
for i in list:
    mul=mul*i
    print(mul)'''

'''list=int(input("enter:"))
for i in range(1,5):
    c=list*i
    print(list,'*',i,'=',c)

n=int(input("Enter"))
for i in range(3,n,3):
    print(i)'''
'''
manju = int(input("Enter the rows:"))
# Outer loop will print number of rows
for i in range(0,manju+1):
# Inner loop will print number of Astrisk
    for j in range(i):
        print(i,end = '')
    print()'''

n=int(input("Enter number:"))
for i in range(1,n+1):
    for j in range(i):
      i=j+1
      print(i,end='')
    print()




