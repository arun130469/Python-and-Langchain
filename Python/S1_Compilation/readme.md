# Machine Code
A CPU runs only instruction set that it is hardwired for by the design of the CPU and cannot be changed. Like the Intel x86 family of processors. 
Machine code is a program written in machine language. It is the lowest level of a program. All programs are converted into machine code before execution.

# 8085 CPU
1. It has 246 instructions each of 8-bit value. Each of them is called an op-code

Therefore its evident that a any program needs to be compiled into a compatible machine code targeting an instruction set. 


# Program
Typically made of many many mechine code instructions. Each machine code instruction is very primitive and basic like adding 2 numbers. 

# How does a program run
1. CPU does "LOAD" and "EXECUTE" - load fetches the op-code and operands (if any) from memory and then execute executes. 

`LD A, 01H` --> `00111110``00000001`

In RAM
`3E` <-- 0000H
`01` <-- 0001H


