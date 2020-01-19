Insert the exam's x86-prime instructions into "test.prime", then execute "run.py".

NB: Remember indentation!

CORRECT:

program:
    subq $16, %rsp
    movq %r11, 8(%rsp)



INCORRECT
program:
subq $16, %rsp
movq %r11, 8(%rsp)
