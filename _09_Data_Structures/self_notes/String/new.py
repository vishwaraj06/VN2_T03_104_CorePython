str2=input("Enter a word:")
if len(str2) <= 1:
 x= str2[1:len(str) - 1]
str2[len(str2) - 1] + x + str2[0]
print("After swaping the word is:",x.swapcase())