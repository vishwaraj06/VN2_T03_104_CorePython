# #*args(non keyword arguments)
# def adder(*num):#*num as a parameter
#     sum = 0
#
#     for n in num:
#         sum = sum + n
#
#     print("Sum:", sum)
# adder(2,3)#  Allows us to pass variable length argument list to the adder() function
# adder(2,3,4,5,6)
# adder(2,5,7)
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1