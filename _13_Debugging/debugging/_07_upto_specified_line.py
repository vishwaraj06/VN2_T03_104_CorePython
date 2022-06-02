# importing pdb
import pdb
# simple function
def fxn(n):
    # set trace
    pdb.set_trace()
    l = []
    for i in range(n):
        l.append(i)
    print(l)
    return


fxn(5)

'''
pdb line no

unt line no



Execute code until the specified line:
--------------------------------------

Use unt to proceed with execution like c, however, stop at the following line more noteworthy 
than the current line. 
Now and then unt is more helpful and faster to utilize and is actually what you need.

unt(il) [lineno]
Without argument, continue execution until the line with a number greater than the current one 
is reached.  

With a line number, continue execution until a line with a number greater or equal to that 
is reached.  In both cases, also stop when the current frame returns.
'''