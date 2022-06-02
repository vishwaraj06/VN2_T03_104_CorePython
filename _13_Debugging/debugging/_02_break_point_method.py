# In a similar way, we can use the breakpoint() method
# (which doesn’t need to import pdb).

# a simple function
def fxn(n):
    for i in range(n):
        print("Hello! ", i + 1)


# using breakpoint c, q, n, s
breakpoint()
fxn(5)  # use pdb n for next line execution