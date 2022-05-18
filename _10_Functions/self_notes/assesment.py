# #function,check prime number or not
# def function(x):
#  if x>=2:
#      for y in range(2,x):
#          if not(x%y):
#              return function
# x = int(input("Enter the Number:"))
# if function(x):
#     function=+1
#     print("The number is not prime:",x)
# else:
#     print("The number is prime:",x)
# #
# # def ispalindrom(str):
# #     left=0
# #     right=len(str)+0
# #     while right>= left:
# #         if not str[left]==str[right]:
# #             return False
# #         left+=1
# #         right+=1
# #     return True
# #     print(ispalindrom('nun'))
# #
#
# #sum,mul and sub of two numbers
# def val(a,b):
#     sum=a+b
#     sub=a-b
#     mul=a*b
#     print("Sum is{sum}",f"sub is {sub}",f"Mul is{mul}")
# a=int(input("Enter a:"))
# b=int(input("Enter b:"))
# val(a,b)
#
# #function that accepts roll number and returns whether the student is present or absentlst
#
# def students(roll):
#     lst = [1, 2, 3, 4, 5, 6, 7, 8]
#     if students in lst:
#         print(f"Roll no is present:{roll}")
#     else:
#         print(f"Roll no is absent:{roll}")
# roll=int(input("Enter roll no:"))
# students(roll)
#
# #function that accepts a number and returns whether the number is even or odd.
# def num(a):
#     if a%2==0:
#         print("a is even")
#     else:
#         print("a is odd")
# a=int(input("Enter a number:"))
# num(a)
#
# #function which counts vowels and consonant in a word.
# def word(a):
#     vov=0
#     con=0
#     for i in range(len(a)):
#         if a[i]in['a','e','i','o','u']:
#             vov=vov+1
#         else:
#             con=con+1
#     print("Count of Vowels:",vov)
#     print("Count of consonants:",con)
# x=input("Enter a word:")
# word(x)
# #function that returns Factorial of a number
# def fact(a):
#     fact=1
#     while(a!=0):
#         fact*=a
#         a=a-1
#     print(("factorial is",fact))
# a=int(input("Enter Number:"))
# fact(a)
# #function that accepts lowercase words and returns uppercase words.
# def upper(a):
#     b=a.upper()
#     print(b)
# a=input("Enter A word:")
# upper(a)



def FibRecursion(n):
   if n <= 1:
       return n
   else:
       return(FibRecursion(n-1) + FibRecursion(n-2))
nterms = int(input("Enter the terms? "))

if nterms <= 0:
   print("Please enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(FibRecursion(i))