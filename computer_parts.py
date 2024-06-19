class ALU:
    # does not just do arithmatic. f good naming
    def __init__(self,a,b,s,func):
        self.a = int(a)
        self.b = int(b)
        self.s = int(s)
        self.func = int(func)
        self.über = 0 #haha tf2 funny
        # func 0 = nothing
        # func 1 = add a and b
        # func 2 = sub a and b
        # func 3 = mult a and b
        # func 4 = div a and b
        # func 5 = bitwise not a
        # func 6 = bitwise and a and b
        # func 7 = bitwise or a and b
                
    def clock(self):
        # clocks the alu
        # runs all the ALU functions
        if self.func == 1:
            self.s = self.a + self.b
        if self.func == 2:
            self.s = self.a - self.b
        if self.func == 3:
            self.s = self.a * self.b
        if self.func == 4:
            self.s = int(self.a / self.b)
        if self.func == 5:
            self.s = ~self.a
        if self.func == 6:
            self.s = self.a & self.b
        if self.func == 7:
            self.s = self.a | self.b
        # checks for overflow
        if self.s > 2147483647:
            self.über = 1
            self.s = self.s - 2147483647
        elif self.s < -2147483648:
            self.über = 1
            self.s = self.s + 2147483647
        else:
            self.über = 0
    
    def test(self):
        # tests all parts of the system.
        # hopefully.
        self.a = 2
        self.b = 1
        
        # what we want
        print("ideal output: 0 ,3 ,1 ,2 ,2 ,-3 ,0 ,3")

        self.func = 0
        self.clock()
        print(self.s,",",end="")
        # should be 0

        self.func = 1
        self.clock()
        print(self.s,",",end="")
        # should be 3

        self.func = 2
        self.clock()
        print(self.s,",",end="")
        # should be 1

        self.func = 3
        self.clock()
        print(self.s,",",end="")
        # should be 2

        self.func = 4
        self.clock()
        print(self.s,",",end="")
        # should be 2

        self.func = 5
        self.clock()
        print(self.s,",",end="")
        # should be -3

        self.func = 6
        self.clock()
        print(self.s,",",end="")
        # should be 0

        self.func = 7
        self.clock()
        print(self.s,end="")
        # should be 3

class Counter:
    # defines a generic counter
    def __init__(self,num):
        self.num = num
    
    def inc(self):
        # increments the counter
        self.num = self.num + 1

    def dec(self):
        # decriments the counter
        self.num = self.num - 1
    
    def set(self, num):
        # sets the counter
        self.num = num

class PRGROM:
    def __init__(self,addr,data,file):
        self.addr = addr
        self.data = data
        self.file = file
    
    def read(self,addr):
        self.data = self.file[addr]
    