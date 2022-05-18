def operation(num1, num2):
    x=num1+num2
    y=num1-num2
    z=num1*num2
    return x, y,z
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
print("Addition & subtraction and Multiplication is:",operation(num1,num2))