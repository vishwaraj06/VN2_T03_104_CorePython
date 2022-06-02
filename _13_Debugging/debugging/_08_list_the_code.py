import pdb  # importing pdb
def fxn(n): # simple function
	l=[]
	for i in range(n):
		l.append(i)
	return
pdb.set_trace() # set trace
fxn(5)

'''
pdb ll

Listing Source code is another feature that can be used to track the code with a line number 
as a list. For this ll command is used.

longlist | ll -> List the whole source code for the current function or frame.


'''