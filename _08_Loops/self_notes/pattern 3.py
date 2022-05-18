'''num=int(input("Enter values:"))
ascii(65)
for i in range(0,num+1):
   for i in range(0,i+1):
        val=chr(ascii)
        print(val,end=" ")
        ascii +=1
    print()
'''

for i in range(65, 70):
  asc=1
# inner loop for jth columns
for j in range(0, i + 1):
    print(chr(asc), end="")
    ascii += 1

print()