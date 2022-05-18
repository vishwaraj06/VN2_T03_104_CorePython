#a variable declared outside of the function or in global scope is known as a global variable.
# This means that a global variable can be accessed inside or outside of the function.
x = "global"
def foo():
    print("x inside:", x)
foo()
print("x outside:", x)

#A variable declared inside the function's body or in the local scope is known as a local variable.

print("**************************")
def foo():
    y = "local"
    print(y)

foo()