'''
Debugging:
The process of identifying and removing errors from source code.

pdb —  Python Debugger¶.
The module pdb defines an interactive source code debugger for Python programs.
It supports setting (conditional) breakpoints and single stepping at the source line level,
inspection of stack frames, source code listing, and evaluation of arbitrary Python code
in the context of any stack frame.

The PDB module in Python used for compelling debugging of Python code. This incorporates:

Pausing of the program
Looking at the execution of each line of code
Checking the values of variables
This module is already installed with installing of python.
So, we only need to import it into our code to use its functionality.
Before that we must know some concepts which are mentioned below:

To import we simply use import pdb in our code.
For debugging, we will use pdb.set_trace() method.
Now, in Python breakpoint() method is also available for this.
We run this on Python idle terminal (you can use any ide terminal to run).
Let’s begin with a simple example consisting of some lines of code.

Example:
'''
# importing pdb
import pdb

# make a simple function to debugg
def fxn(n):
    pdb.set_trace()
    for i in range(n):
        print("Hello! ", i+1)


# starting point to debugg

fxn(5)

'''
Here, we can see that when the function call is done then pdb executes and ask 
for the next command. We can use some commands here like 

c -> continue execution

q -> quit the debugger/execution

n -> step to next line within the same function

s -> step to next line in this function or a called function

pdb help ->
Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt      
alias  clear      disable  ignore    longlist  r        source   until    
args   commands   display  interact  n         restart  step     up       
b      condition  down     j         next      return   tbreak   w        
break  cont       enable   jump      p         retval   u        whatis   
bt     continue   exit     l         pp        run      unalias  where    

Miscellaneous help topics:
==========================
exec  pdb


'''
