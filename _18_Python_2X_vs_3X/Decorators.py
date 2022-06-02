# #decorator is a special type of function which  behavior of the function without modifying the functionality of the functions
# #example: when we call a function,it accepts the input from the other functions
# #before we need to work on decorators we need to know about nested functions
# # def outer():
# #   print("I'm the outer function.")
# #   def inner():
# #     print("And I'm the inner function.")
# #   inner()
# # #inner()
# #outer()
# def dec(new): #new as arguments
#     def a1():
#         print("Hi")
#         new()
#         print("Thanks")
#     return a1
# @dec  #We are going to use this decorator in our functions
# def decorator():
#     print("Good Mrng")
# #decorator=dec(decorator)#method giving  assignment to the function and giving input as decorator
# decorator()