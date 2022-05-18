'''#1.reverse a srting:
word=input("Enter a word:")
def reverse(word):
    if len(word)==0:
        return word
    else:
        return reverse(word[1:])+word[0]
print("Reverse of string is:",reverse(word))
def sum_list(lst):
  sum = 0
  for x in lst:
    sum=sum+x
  return sum

lst=[1,2,3,4,5]
print(sum_list(lst))

#2. sum all the numbers in a list

def add(lst):
    sum =0
    for i in lst:
     sum=sum+lst
    return sum
lst=[21,34,55,12,89,67]
print("Addition of Entire list:",sum(lst))

#3 Multiplication of list

def multiplication(lst):
    mul=1
    for i in lst:
        mul=mul*i
    return mul
lst1=[4,5,6,1]
print("Multiply of List:",multiplication(lst1))

#4 factorial of the Given number
def fact(a):
    fact=1
    while(a!=0):
        fact*=a
        a=a-1
    print(("factorial is:",fact))
a=int(input("Enter Number:"))
fact(a)
nums = [1, 34, 23, 56, 89, 44, 92]
odds = list(filter(lambda x: x % 2 == 0, nums))
print("Map:", odds)
#6. even and odd number:

def num(a):
    if a%2==0:
        print("a is even")
    else:
        print("a is odd")
a=int(input("Enter a number:"))
num(a)


#5 Even Number in the list
nums = [1,2,3,4,5,6,7,8,9,10]
Even = list(filter(lambda x: x % 2 == 0, nums))
print("Even number in the List:", Even)'''

#6.pascal triangle


