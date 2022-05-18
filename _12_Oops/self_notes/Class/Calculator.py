class Calculator():
    def add(self):
        print(a+b)
    def sub(self):
        print(a-b)
    def mul(self):
        print(a*b)
    def div(self):
        print(a/b)
a = int(input("Enter first number:"))
b = int(input("Enter first number:"))
obj = Calculator
choice=1
while choice!=0:
    print("1.ADD")
    print("2.SUB")
    print("3.MUL")
    print("4.DIV")
    choice=int(input("Enter your choice:"))
    if choice==1:
      print(obj.add(choice))
    elif choice==2:
      print(obj.sub(choice))
    elif choice==3:
      print(obj.mul(choice))
    elif choice==4:
      print(obj.div(choice))
    else:
      print("INVALID CHOICE")
