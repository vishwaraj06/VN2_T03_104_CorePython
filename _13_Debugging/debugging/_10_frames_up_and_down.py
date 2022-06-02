# importing pdb
import pdb

# simple function
def fxn(i):
	print(i)
	return

# set trace
pdb.set_trace()
for i in range(5):
	fxn(i)
'''
d - moves to newest frame
u - moves to oldest frame


Here, we can play with each trace as a frame, and we can also move from one frame to another.


w(here)
Print a stack trace, with the most recent frame at the bottom. 
An arrow indicates the “current frame”, which determines the context of most commands.  
‘bt’ is an alias for this command.

u(p) [count]
Move the current frame count (default one) levels up in the stack trace (to an older frame).

d(own) [count]
Move the current frame count (default one) levels down in the stack trace (to a newer frame).

'''