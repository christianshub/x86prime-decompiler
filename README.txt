- Description:
x86prime is a x86 subset for learning the basics of assembly. The tool has been created by Finn Schiermer Andersen
and Michael Kirkedal Thomsen 2018 (https://github.com/finnschiermer/x86prime). Documentation can be found at
https://x86prime.github.io/x86prime/

x86prime-asm-translation assists in translating each instruction for a better overview of the entire structure of the
assembly code in question.

---------------------------------------------------------------------------------------------------
- How-to:

Insert the x86-prime instructions into "test.prime", then execute "run.py".

---------------------------------------------------------------------------------------------------
- Example before run.py:

program:
subq $16, %rsp
movq %r11, 8(%rsp)
movq %rbx, (%rsp)
movq %rdi, %rbx
movq %rsi, %rax
cbe $1, %rsi, .L2
leaq -1(%rsi), %rsi
call power, %r11
.L2:
imulq %rbx, %rax
movq (%rsp), %rbx
movq 8(%rsp), %r11
addq $16, %rsp
ret %r11

---------------------------------------------------------------------------------------------------
- Example after run.py:

Line  1: program:                        # Line 1: function
Line  2: subq $16, %rsp                  # Line 2: %rsp = %rsp minus (-) $16
Line  3: movq %r11, 8(%rsp)              # Line 3: 8(%rsp) = %r11
Line  4: movq %rbx, (%rsp)               # Line 4: (%rsp) = %rbx
Line  5: movq %rdi, %rbx                 # Line 5: %rbx = %rdi
Line  6: movq %rsi, %rax                 # Line 6: %rax = %rsi
Line  7: cbe $1, %rsi, .L2               # Line 7: if $1 == %rsi then jump to .L2
Line  8: leaq -1(%rsi), %rsi             # Line 8: -1 + (%rsi) -> %rsi (Add a constant)
Line  9: call power, %r11                # Line 9: calling power, and storing return address in %r11
Line 10: .L2:                            # Line 10: .L2:

==== .L2: =============================================================
Line 11: imulq %rbx, %rax                # Line 11: %rax = %rax unsigned multiplicate (*) %rbx
Line 12: movq (%rsp), %rbx               # Line 12: %rbx = (%rsp)
Line 13: movq 8(%rsp), %r11              # Line 13: %r11 = 8(%rsp)
Line 14: addq $16, %rsp                  # Line 14: %rsp = %rsp add (+) $16
Line 15: ret %r11                        # Line 15: return %r11
