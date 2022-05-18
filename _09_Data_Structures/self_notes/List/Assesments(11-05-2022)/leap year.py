class Leap:
    def new(self,x):
        if x % 4 == 0 and x % 100 != 0:
            return 1
        elif x % 400 == 0:
            return 1
print("Enter the Year: ", end="")
x = int(input())

ob1 = Leap()
ob2= ob1.new(x)
if ob2==1:
    print("Leap Year")
else:
    print("Not a Leap Year")
'''
    if y % 4 == 0 and y % 100 != 0:
            return 1
        elif y % 400 == 0:
            return 1'''