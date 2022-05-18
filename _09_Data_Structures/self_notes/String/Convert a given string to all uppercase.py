#1.build in methods
x="We are indians"
y=x.upper()
print(y)

#2.loops:
str="we are indians"
str1=""
for i in str:
    if(i>='a' and i<='z'):
        str1=str1+chr((ord(i)-32))
    else:
        str1=str1+i
print("upper case:",str1)



