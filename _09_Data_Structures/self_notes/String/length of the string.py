# Length of the string

#1.build in method
str="We are indians"
print("Lenghth of the string is:",len(str) )

#2.functions
def func(str):
   counter=0
   for i in str:
    counter+=1
   return  counter
str='we are indians'
print(str)
str1=str.count('str')
print("count of i is:",str1)

#3 loops:
i=input("Enter any thing:")
a=0
for j in i:
 a+=1
print(a)

#4 if else:

'''

#3. String slice
print("slice is:",str[8:11])

#4. length of the longest string
print("Longest string:",max(str,key=len))
'''