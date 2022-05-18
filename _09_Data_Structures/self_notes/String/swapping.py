#1.functions
def swap(x):
    x=list(x)
    for i in range(0,len(x)-1,2):
        x[i],x[i+1]=x[i+1],x[i]
        return "".join(x)
x="HELLO"
print(swap(x))

'''#2 in build mehod
a="hi"
b="hello"
temp=a
a=b
b=temp
print("After swapping a is:",a)
print("After swapping b is:",b)'''

strin1="AbCdEfGh"
print(strin1.swapcase())



