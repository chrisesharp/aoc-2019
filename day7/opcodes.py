from math import floor

class Processor():
    memory = []
    ip = 0
    stdin = None
    stdout = []
    op_parms = { 1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4 }

    def __init__(self, instructions):
        self.memory = instructions[:]
        self.ip = 0
        self.stdin = None
        self.stdout = []
        
    
    def run(self, stdin):
        self.set_std_input(stdin)
        instruction = self.step()
        while instruction:
            instruction = self.step()
        return self.stdout.pop()

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
        next_ip = self.ip + self.op_parms[opcode]
        instruction = self.memory[self.ip:next_ip]
        self.ip = next_ip
        return instruction

    def get_opcode(self):
        return self.memory[self.ip]%100
    
    def execute(self, instr):
        opcode, mode, parms = decode(instr)
        A, B, C = self.demarshall(parms, mode)
        if opcode == 1:
            self.memory[C] = A + B
        elif opcode == 2:
            self.memory[C] = A * B
        elif opcode == 3:
            A = self.get_parm(parms[0],1)
            input = self.stdin.pop()
            self.memory[A] = input
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
        
    def get_parm(self, parm, immediate):
        if immediate:
            value = parm
        else:
            value = self.memory[parm]
        return value
    
    def demarshall(self, parms, modes):
        result = [0,0,0]
        for i in range(len(parms)):
            p = parms[i]
            m = modes[i]
            result[i] = self.get_parm(p, m)
        return list(result)

def get_mode(instr):
    mode = floor(instr/100)
    flags = [0,0,1]
    for i in range(len(flags)-1):
        flags[i] = mode%10
        mode = floor(mode/10)
    return flags

def decode(instr):
    return instr[0]%100, get_mode(instr[0]), instr[1:]

def get_program(file):
    with open(file) as f:
        return list(map(int, f.read().split(',')))

def get_phase_permutations(phases):
    phase_perms = [[]]
    for n in phases:
        new_perm = []
        for perm in phase_perms:
            for i in range(len(perm) + 1):
                new_perm.append(perm[:i] + [n] + perm[i:])
                phase_perms = new_perm
    return phase_perms

class Amps():
    inputs = [[],[],[],[],[]]
    outputs = [[],[],[],[],[]]
    procs = [0,0,0,0,0]

    def __init__(self, prog, inp, phases):
        self.inputs = [[],[],[],[],[]]
        self.outputs = [[],[],[],[],[]]
        self.procs = [0,0,0,0,0]
        self.inputs[0].append(inp)
        for i in range(5):
            self.inputs[i].append(phases[i])
            self.procs[i] = Processor(prog)
            self.procs[i].set_std_input(self.inputs[i])
    
    def start(self):
        i=0
        output = None
        running = [True, True, True, True, True]
        while running[i]:
            output_written = False
            while running[i] and not output_written:
                instruction = self.procs[i].step()
                running[i] = (instruction != None)
                output = self.procs[i].get_std_output()
                output_written = (output != None)
            if output != None:
                self.outputs[i].append(output)
            i = (i+1)%5
            if output != None:
                self.inputs[i].insert(0,output)
        return self.outputs[4].pop()

if __name__ == '__main__':
    file = "input.txt"
    prog = get_program(file)
    
    best = None
    optimal = 0
    output = 0
    phase_perms = get_phase_permutations(range(0, 5))
    for phases in phase_perms:
        input = [0]
        for setting in phases:
            processor = Processor(prog)
            input.append(setting)
            output = processor.run(input)
            input = [output]
        if output > optimal:
            optimal = output
            best = phases[:]
    print("Part 1:")
    print(optimal)
    
    print("Part 2:")
    best = None
    optimal = 0
    output = 0
    phase_perms = get_phase_permutations(range(5, 10))
    for phases in phase_perms:
        amps = Amps(prog, 0, phases)
        output = amps.start()
        if output > optimal:
            optimal = output
            best = phases[:]
    print(optimal)
    