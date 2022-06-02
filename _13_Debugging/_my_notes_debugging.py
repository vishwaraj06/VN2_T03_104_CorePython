
import pdb
# print 1 to 100 numbers
i = 0
count = 0
while i <= 100:
    if i % 2 == 0:
        print("even numbers:", i)
        count += 1
    if count == 10:
        break
    i += 1
pdb.set_trace()
i = 0
count = 0
for i in range(1, 100):
    if i % 2 != 0:
        print("odd numbers:", i)
        count += 1
    if count == 10:
        pass
    if count == 25:
        break
    i += 1

'''
Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt
alias  clear      disable  ignore    longlist  r        source   until
args   commands   display  interact  n         restart  step     up
b      condition  down     j         next      return   tbreak   w
break  cont       enable   jump      p         retval   u        whatis
bt     continue   exit     l         pp        run      unalias  where



# pdb module : pdb.set_trace()
The module pdb defines an interactive source code debugger for Python programs.It supports setting(conditional) 
breakpoints and single stepping at the source line level,inspection of stack frames, source code listing, 
and evaluation of arbitrary Python code in the context of any stack frame.

In order to run the debugger just type c and press enter. As the same suggests, PDB means Python debugger.
 To use the PDB in the program we have to use one of its method named set_trace() 

1 pdb.run: (statement, globals = None, locals= None)
Execute the statement under debugger control, using debugger prompt  setting break points and type continue

2.pdb.runeval: evaluate the expression under debugger control and return final value  
runeval(expression, globals=None, locals=None)

3.pdb.runcall: call the function with given arguments and return the function 
runcall(function, *args, **kwds)

4.pdb.set_trace: enter the debugger calling stack frame.This is useful to hardcode a breakpoint at a given point
in a program. Even if the code is not  being bugged ,when assertion fails.even if given header is printed to console
just debugging begins

5.pdb.post_mortem:(traceback = None)
Enter postmortem for debugging the given traceback object.if no traceback is given ,it uses the exception which is 
currently being handled

6.pdb.pm()
Enter the post mortem debugging of the last traceback found in  sys.last_traceback

7.h(elp): help pdb
with argument display the available commands

8.w(here):
print a stack frame with the most recent frame at the bottom,An arrow indicates the current frame, which
determines the context of the most commands

9.d(own):
move the current frame count level down in the stack trace(new line).

10.u(p):
move the current frame count level up in the stack trace(older line).

11. b(reak): [([filename:]lineno | function) [, condition]]
with lineno argument set breakpoint in current file.with function argument set a break point in first executable
statement with that function .the line number may be prefixed with number and a colon to specify a break point in 
another file.Th file is searched on sys.path.

12.tbreak:
temporary break point which is removed automatically when it is first hit, arguments are same for break

13.cl(ear): [filename:lineno | bpnumber ...]
with filename:lineno arguments clear all the break points at this line.with a space seperated list of breakpoints
numbers clear all break points.without argument clear all breaks

14.disable:
disabling the breakpoint number means it cannot cause the program to stop execution, unlike it clearing breakpoint
it remains in the list of breakpoints and it re(enabled)

15. enable:
enable the breakpoints specified

16.ignore:
set the ignore count for break point if count is omitted and if it it s set to be 0 ,then breakpoint becomes active

17.condition:
set a new condition for the breakpoint which  an expression is evaluated to be true, before the breakpoint is honoured.
if condition is absent any existing condition is removed i.e breakpoint made unconditional

18. command:
Specify a list of commands for breakpoint number bpnumber. The commands themselves appear on the following lines.
 Type a line containing just "end" to terminate the commands.
To remove all commands from a breakpoint, type commands and follow it immediately with end; that is, give no commands.

With no bpnumber argument, commands refers to the last breakpoint set. 
You can use breakpoint commands to start your program up again. Simply use the continue command, or step,
 or any other command that resumes execution

1.s(tep):Execute the current line and stop at the first possible occasion

2.n(ext):
Execution done until next line reaches or return in function.(step) stops the execution in called function and 
next starts execution  in the called function with full speed ,only stopping at next line in the same function

3.unt(il):
Without argument, continue execution until the line with a number greater than the current one is reached.
With a line number, continue execution until a line with a number greater or equal to that is reached. In both cases,
also stop when the current frame returns.

4.r(eturn):
continue execution until current function returns

5.c(ont(inue)):
continue execution, only stop when breakpoint is encountered

6.j(ump):
Set the next line that will be executed. Only available in the bottom-most frame. This lets you jump back and 
execute code again, or jump forward to skip code that you don’t want to run.
It should be noted that not all jumps are allowed – for instance it is not possible to jump into the middle of 
a for loop or out of a finally clause

7.l(ist):
List source code for the current file. Without arguments, list 11 lines around the current line or continue the 
previous listing. With . as argument, list 11 lines around the current line. With one argument, list 11 lines 
around at that line. With two arguments, list the given range; if the second argument is less than the first, 
it is interpreted as a count.

The current line in the current frame is indicated by ->. If an exception is being debugged, the line where the 
exception was originally raised or propagated is indicated by >>, if it differs from the current line.

8.ll:long list
list all source code for current frame or function. interesting lines are marked up with list

9.a(rgs):
print the current list of arguments

10.p (expression):
Evaluate the current expression and print its value

11.pp (expression)
evaluate the expression ,except print the value it pretty printed the ppmodule

12.what is (expression):
type of expression

13.source :
try to get source code for an object and display it

14.display:
display the value of expression if it is changed stops at the next line

15. undisplay
do not display the value of expression any more in the current line

16.interact:
start an interactive interpreter whose global space contain all the local and global names found in current scope

17 alias:
Create an alias called name that executes command. The command must not be enclosed in quotes. Replaceable parameters 
can be indicated by %1, %2, and so on, while %* is replaced by all the parameters. If no command is given, the current
 alias for name is shown. If no arguments are given, all aliases are listed.

Aliases may be nested and can contain anything that can be legally typed at the pdb prompt. Note that internal pdb
 commands can be overridden by aliases. Such a command is then hidden until the alias is removed. Aliasing is 
 recursively applied to the first word of the command line; all other words in the line are left alone.
 
18.unalias:
delete the special alias

19.run (args)
20.restart(args):
Restart the debugged Python program. If an argument is supplied, it is split with shlex and the result is used as
the new sys.argv. History, breakpoints, actions and debugger options are preserved. restart is an alias for run.
 
21.q(uit):
quit from debugger and aborts th execution

22.de(bugger)
enter recursive debugger mode that steps through the code argument

23.footnotes:
Whether a frame is considered to originate in a certain module is determined by the __name__ in the frame globals

24.retval:
print the return value for last return of  function























'''
pdb.help()




