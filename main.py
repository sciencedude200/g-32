import computer_parts
import prg
import ram
# imports computer parts

a = 0
b = 0
c = 0
d = 0
s = 0
# defies the registers

alu = computer_parts.ALU(0,0,0,0)
prgcnt = computer_parts.Counter(0)
ramcnt = computer_parts.Counter(0)
ram = computer_parts.RAM(0,0,ram.ram)
rom = computer_parts.ROM(0,0,prg.prg)
# defines all the parts