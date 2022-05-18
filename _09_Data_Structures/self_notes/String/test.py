def func(str1):
   counter=0
   for i in str1:
       print(i)
       counter+=1
   return  counter
str1='we'
#str1=str.count('str')
c1=func(str1)
print(c1)
print("count of i is:",c1)
