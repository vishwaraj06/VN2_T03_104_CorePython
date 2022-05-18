print("***** total number of working days is 100*****")
a=int(input("Enter Number of Days present:"))
b=int(input("Enter Number of days absent:"))
if  a>75 and b<75:
   c=a+b/100
   print(c,"Percentage is")
#else:
 #   print("enter the valid data")
if c >= 75:
      print("You are eligible to attend exam \n Thank you")
else:
 print("You are not eligible to attend exam\n Thank you")



