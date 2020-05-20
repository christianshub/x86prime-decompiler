## What is x86prime
x86prime was created by Finn Schiermer Andersen and Michael Kirkedal Thomsen in 2018. x86prime is a x86 subset created to learn DIKU students the basics of x86 assembly. 

- x86prime repo: https://github.com/finnschiermer/x86prime
- documentation: https://x86prime.github.io/x86prime/

## What is x86prime-asm-translation
This tool adds a comment on each line of what each instruction mean. 

## How-to

Insert the x86-prime instructions into "test.prime", then execute "run.py".

## Usage example

#### before run.py:

```asm
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
```

#### Example after run.py:

```asm
Line  1: program:                        # function
Line  2: subq $16, %rsp                  # %rsp = %rsp minus (-) $16
Line  3: movq %r11, 8(%rsp)              # 8(%rsp) = %r11
Line  4: movq %rbx, (%rsp)               # (%rsp) = %rbx
Line  5: movq %rdi, %rbx                 # %rbx = %rdi
Line  6: movq %rsi, %rax                 # %rax = %rsi
Line  7: cbe $1, %rsi, .L2               # if $1 == %rsi then jump to .L2
Line  8: leaq -1(%rsi), %rsi             # -1 + (%rsi) -> %rsi (Add a constant)
Line  9: call power, %r11                # calling power, and storing return address in %r11
Line 10: .L2:                            # .L2:

==== .L2: =============================================================
Line 11: imulq %rbx, %rax                # %rax = %rax unsigned multiplicate (*) %rbx
Line 12: movq (%rsp), %rbx               # %rbx = (%rsp)
Line 13: movq 8(%rsp), %r11              # %r11 = 8(%rsp)
Line 14: addq $16, %rsp                  # %rsp = %rsp add (+) $16
Line 15: ret %r11                        # return %r11
```
