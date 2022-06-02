'''
Features provided by PDB Debugging:
----------------------------------------
1. Printing Variables or expressions

When utilizing the print order p, you’re passing an articulation to be assessed by Python.
On the off chance that you pass a variable name, pdb prints its present worth.
Notwithstanding, you can do considerably more to examine the condition of your running application.

An application of PDB debugging in the recursion to check variables

In this example, we will define a recursive function with pdb trace and check the values of variables
at each recursive call. To the print the value of variable,
we will use a simple print keyword with the variable name.


'''

# importing pdb
import pdb
# define recursive function
def rec_fxn(r):
    if r > 0:
        # set trace
        pdb.set_trace()
        rec_fxn(r // 2)
    else:
        print("recursion stops")
    return
# set trace at start,   use n, print(r)
pdb.set_trace()
rec_fxn(5)

#use pdb n,
# print(r) returns n input 5 which passess argument in function call
# pdb n
# print(r) returns after using floor division operator n = 2
# pdb n
# print(r) returns r = 1
# pdb n
# returns recursion


# In Python, recursion is the process of a function calling itself directly or indirectly.
# This is a way to get to the solution of a problem by breaking it into smaller and simpler steps