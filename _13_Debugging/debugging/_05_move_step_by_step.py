'''
Moving in code by steps

This is the most important feature provided by pdb. The two main commands are used for this which are given below:

n -> step to next line within the same function

s -> step to next line in this function or a called function

Let’s understand the working of these with the help of an example.
'''
# importing pdb
import pdb

# simple function
def fxn(n):
    l = []
    for i in range(n):
        l.append(i)
    return


# set trace
pdb.set_trace()
fxn(5)
