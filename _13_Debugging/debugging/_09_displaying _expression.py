# importing pdb
import pdb
# simple function
def fxn(n):
    l = []
    for i in range(n):
        l.append(i)
    # set trace
    pdb.set_trace()
    print(l)
    return
fxn(5)


'''
display
display l
display [x*x for x in l]
undisplay
undisplay [x*x for x in l]

Displaying Expressions:
-------------------------

Like printing articulations with p and pp, you can utilize the order show [expression] 
to advise pdb to consequently show the estimation of an articulation, 
on the off chance that it changed, when execution stops. 
Utilize the order undisplay [expression] to clear a showcase articulation.

display [expression]
Display the value of the expression if it changed, each time execution stops in the current frame.
 Without expression, list all display expressions for the current frame.

undisplay [expression]
Do not display the expression any more in the current frame. Without expression, 
clear all display expressions for the current frame.
'''