from arithmetic.addq   import addq
from arithmetic.subq   import subq
from arithmetic.andq   import andq
from arithmetic.orq    import orq 
from arithmetic.xorq   import xorq
from arithmetic.imulq  import imulq
from arithmetic.mulq   import mulq
from arithmetic.salq   import salq
from arithmetic.sarq   import sarq
from arithmetic.shrq   import shrq

def arithmetic(string):
    addq(string)
    andq(string) 
    imulq(string)
    mulq(string)
    orq(string) 
    salq(string)
    sarq(string)
    shrq(string) 
    subq(string) 
    xorq(string)


