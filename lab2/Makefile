
all : run-fifo run-sc

machine : machine.c
	gcc -std=c99 -Wall $< -o $@

debug : machine.c
	gcc -std=c99 -g -O0 -Wall -DDEBUG machine.c -o machine

run-fifo : machine
	./machine --fifo fac.s

run-sc : machine
	./machine --second-chance fac.s

clean :
	rm -f machine
