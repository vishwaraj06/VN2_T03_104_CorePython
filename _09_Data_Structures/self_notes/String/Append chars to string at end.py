#1.inbuild methods:
strin="Hello"
strin1="Raj"
strin3=strin+strin1
print(strin3)

#2.loops:
list1=["hello","How","are","you"]
strin4=""
for i in list1:
    strin4+=str(i)
print("After append:",strin4)

#3.functions
def append(a,b,c):
    if len(a)>4 and a[-5]=='':
        return a+c
    return a+b+c
print("append:",append('raja','gowri','tharun'))
