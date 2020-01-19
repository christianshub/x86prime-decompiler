# DONT TOUCH ANYTHING HERE, INSERT EXAM x86-prime ASSEMBLY INTO test.prime :-) 
from arithmetic.arithmetic import arithmetic
from jmp.jmp import jmp
from mov.mov import mov
from other.label import label
from other.startFunc import startfunc
from other.leaq import leaq
from other.ret import ret
from other.call import call
from cb.compareBranch import compareBranch
import os
import sys 

def evaluate(string):
    startfunc(string)
    arithmetic(string)
    mov(string)
    jmp(string)
    label(string)
    leaq(string)
    compareBranch(string)
    ret(string)
    call(string)
    
filepath = os.path.join(sys.path[0], 'test.prime')
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       sline = line.strip()

       print("Line {0:2}: {1} {2} {3}".format(cnt, sline, " "*(30 - len(sline)), "# Line " + str(cnt) + ": "), end = "")
       evaluate(sline)
       print("")
    
       line = fp.readline()
       cnt += 1


