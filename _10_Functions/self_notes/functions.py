def function():
    print("hello")
function()
function()  # calling function
function()
function()
function()
print("*************return statements*********************")

def mul(a=20,b=60):
    #a=12
   # b=20          #return statements
    c=a*b
    return c
print("Multiplication :",mul())
print("*Arguments***")
def name(firstname):
    print("hi",firstname)
name('raja')
name('san')
name('mani')
print("**********************")
def name(fname):
    print("Raj"+fname)
name("email")
name("id")

print("**********************************")
def add(n1,n2):
    print("Addition is",n1+n2)
add(89,67)

print("**********************************")

def sum(num1, num2):
    x = num1 + num2
    return x
print("Addition:",sum(12,20))
print("Addition:",sum(45,89))



