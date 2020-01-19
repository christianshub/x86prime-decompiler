GCC = gcc -S -O3 -fno-optimize-sibling-calls 

all: test_s test_prime test_hex test_run

test_s: test.c
	$(GCC) test.c

test_prime: test.s
	primify test.s && rm -f test.s

test_hex: test.prime
	prasm test.prime

test_run: test.hex
	prun test.hex main -show

clean:
	rm -f *.s *.prime *.hex *.sym
