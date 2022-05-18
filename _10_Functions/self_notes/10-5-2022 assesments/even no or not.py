n=int(input("Enter any number:"))
def even(n):
    if (n == 0):
        return True
    elif (n == 1):
        return False
    else:
        return even(n - 2)

if (even(n)):
    print( "num is even",n)
else:
    print("num is odd:",n)
