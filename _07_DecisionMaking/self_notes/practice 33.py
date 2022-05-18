a=int(input("Enter salary:"))
b=int(input("Service period:"))
if  b>10:
    a=a/b*100
    print( "Your bonus is 10% and total amount is:",a)
elif b >=6 and b<=10:
    a=a/b*100
    print("your bonus is 8% and total amount is:",a)
elif  b<6:
    a=a/b*100
    print("Your bonus is 6% and total ammout is :",a)





