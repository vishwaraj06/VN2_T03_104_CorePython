'''
An Example to check expressions

This example is similar to the above example, that prints the values of expressions
after their evaluation.
'''
# importing pdb
import pdb

# simple function
def fxn(n):
    l=[]
    for i in range(n):
        l.append(i)

    # set trace
    pdb.set_trace()
    return

fxn(10)

# use
# print l, p l, p n,
# p[x*x for x in l]  for squares entire list
# p"".join([str(x) for x in l]) to convert entire list entities in list to str
# pdb n




