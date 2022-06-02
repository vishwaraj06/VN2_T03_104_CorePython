'''
Using Breakpoints

This feature helps us to create breakpoints dynamically at a particular line in the source code.
 Here, in this example, we are creating breakpoint using command b which given below:

b(reak) [ ([filename:]lineno | function) [, condition] ]
--------        Without argument, list all breaks.
With a line number argument, set a break at this line in the current file.

With a function name, set a break at the first executable line of that function.

If a second argument is present, it is a string specifying an expression that must
evaluate to true before the breakpoint is honored.

The line number may be prefixed with a filename and a colon, to specify a breakpoint in
another file (probably one that hasn’t been loaded yet).
The file is searched for on sys.path; the .py suffix may be omitted.
'''
# importing pdb
import pdb

# simple function
def fxn(n):
    list = []

    for i in range(n):
        list.append(i)
    print(list)
    return


# set trace
pdb.set_trace()
fxn(5)

'''
pdb b 9
pdb n
pdb n
l
'''