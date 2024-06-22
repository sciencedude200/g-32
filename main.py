import computer_parts
import prg

# configurations of parts
ram_size = 1000

# defines the registers
a = 0
b = 0
c = 0
d = 0
s = 0

# defines all the parts
alu = computer_parts.ALU(0,0,0,0)
prgcnt = computer_parts.Counter(0)
ramcnt = computer_parts.Counter(0)
ram = computer_parts.RAM(ram_size)
rom = computer_parts.ROM(prg.prg)



# test RAM 
test_value=1234
test_address=12

ram.write(test_address, test_value)
print("RAM test")
print("Written value should be "+ str(test_value))
print("Read data is "+str(ram.read(test_address)))

# test ROM 
test_address=2
print("ROM test")
print("Read only value should be 1234" )
print("Read data is "+str(rom.read(test_address)))
