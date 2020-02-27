from math import floor

class Processor():
    memory = []
    protected = False
    ip = 0
    rb = 0
    stdin = None
    stdout = []
    op_parms_rws = {    1: [ 4, [0,0,1] ],
                        2: [ 4, [0,0,1] ], 
                        3: [ 2, [1] ], 
                        4: [ 2, [0] ], 
                        5: [ 3, [0,0] ], 
                        6: [ 3, [0,0] ], 
                        7: [ 4, [0,0,1] ], 
                        8: [ 4, [0,0,1] ], 
                        9: [ 2, [0] ]
                    }

    def __init__(self, instructions, memory_size = 0, protected = False):
        self.memory = instructions[:]
        self.protected = protected
        for _ in range(memory_size):
            self.memory.append(0)
        self.ip = 0
        self.stdin = None
        self.stdout = []
        
    
    def run(self, stdin):
        self.set_std_input(stdin)
        instruction = self.step()
        while instruction:
            instruction = self.step()
        return self.stdout
    
    def run_to_output(self, input=None):
        if input:
            self.stdin.append(input)
        output = None
        while self.step():
            output = self.get_std_output()
            if output != None:
                break
        return output

    def set_std_input(self, stdin):
        self.stdin = stdin

    def get_std_output(self):
        if len(self.stdout) > 0:
            return self.stdout.pop()
        return None
    
    def step(self):
        instruction = self.fetch()
        if instruction:
            self.execute(instruction)
        return instruction
    
    def fetch(self):
        opcode = self.get_opcode()
        if opcode == 99:
            return None
        next_ip = self.ip + self.op_parms_rws[opcode][0]
        instruction = self.memory[self.ip:next_ip]
        self.ip = next_ip
        return instruction

    def get_opcode(self):
        return self.memory[self.ip]%100
    
    def execute(self, instr):
        opcode, mode, parms = decode(instr)
        A, B, C = self.demarshall(parms, mode, self.op_parms_rws[opcode][1])
        if opcode == 1:
            self.memory[C] = A + B
        elif opcode == 2:
            self.memory[C] = A * B
        elif opcode == 3:
            self.memory[A] = self.stdin.pop()
        elif opcode == 4:
            self.stdout.append(A)
        elif opcode == 5:
            if A != 0: self.ip = B
        elif opcode == 6:
            if A == 0: self.ip = B
        elif opcode == 7:
            self.memory[C] = int(A < B)
        elif opcode == 8:
            self.memory[C] = int(A == B)
        elif opcode == 9:
            self.rb += A

    def get_parm(self, parm, mode, write=False):
        if mode == 1 or (write and mode==0):
            return parm
        if write and mode==2:
            return self.rb + parm
        if mode ==2:
            return self.memory[self.rb + parm]
        return self.memory[parm]

    
    def demarshall(self, parms, modes, writes):
        result = [0,0,0]
        for i in range(len(parms)):
            p = parms[i]
            m = modes[i]
            result[i] = self.get_parm(p, m, writes[i])
        return list(result)

def get_mode(instr):
    mode = floor(instr/100)
    flags = [0,0,0]
    for i in range(len(flags)):
        flags[i] = mode%10
        mode = floor(mode/10)
    return flags

def decode(instr):
    return instr[0]%100, get_mode(instr[0]), instr[1:]

def get_program(file):
    with open(file) as f:
        return list(map(int, f.read().split(',')))
    