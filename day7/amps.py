from opcodes import Processor, get_program
import itertools

class Amps():
    inputs = [[],[],[],[],[]]
    outputs = [[],[],[],[],[]]
    procs = [0,0,0,0,0]

    def __init__(self, prog, inp, phases):
        count = len(phases)
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
        running = [True] * len(self.procs)
        while running[i]:
            output_written = False
            while running[i] and not output_written:
                instruction = self.procs[i].step()
                running[i] = (instruction != None)
                output = self.procs[i].get_std_output()
                output_written = (output != None)
            if output_written:
                self.outputs[i].append(output)
            i = (i + 1) % len(running)
            if output_written :
                self.inputs[i].insert(0,output)
        return self.outputs[4].pop()
    
def run_amps(prog, phase_perms):
    best = None
    optimal = 0
    output = 0

    for phases in list(itertools.permutations(phase_perms)):
        amps = Amps(prog, 0, phases)
        output = amps.start()
        if output > optimal:
            optimal = output
            best = phases[:]
    return optimal


if __name__ == '__main__':
    prog = get_program("input.txt")
    print("Part 1:", run_amps(prog, range(0,5)))
    print("Part 2:", run_amps(prog, range(5,10)))
    