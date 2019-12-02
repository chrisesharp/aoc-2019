def execute(instr, memory):
    op = int(instr[0])
    A = int(instr[1])
    B = int(instr[2])
    C = int(instr[3])

    if op == 1:
        memory[C] = memory[A] + memory[B]
    elif op == 2:
        memory[C] = memory[A] * memory[B]
    return memory

def fetch(instructions):
    adv = 4
    if instructions[0] == 99:
        adv = 1
    return instructions[:4], adv

def run(instructions):
    ip=0
    instr, adv = fetch(instructions)
    while instr[0] != 99:
        ip += adv
        instructions = execute(instr, instructions)
        instr, adv = fetch(instructions[ip:])
    return instructions

def program(instructions, noun, verb):
    prog = instructions[:]
    prog[1] = noun
    prog[2] = verb
    return prog

if __name__ == '__main__':
    instructions = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,5,19,23,1,23,5,27,2,27,10,31,1,5,31,35,2,35,6,39,1,6,39,43,2,13,43,47,2,9,47,51,1,6,51,55,1,55,9,59,2,6,59,63,1,5,63,67,2,67,13,71,1,9,71,75,1,75,9,79,2,79,10,83,1,6,83,87,1,5,87,91,1,6,91,95,1,95,13,99,1,10,99,103,2,6,103,107,1,107,5,111,1,111,13,115,1,115,13,119,1,13,119,123,2,123,13,127,1,127,6,131,1,131,9,135,1,5,135,139,2,139,6,143,2,6,143,147,1,5,147,151,1,151,2,155,1,9,155,0,99,2,14,0,0]
    noun = 12
    verb = 2
    prog1 = program(instructions, noun, verb)
    print("Part 1:")
    print(run(prog1)[0])

    print("Part 2:")
    for noun in range(100):
        for verb in range(100):
            prog = program(instructions, noun, verb)
            output = run(prog)[0]
            if output == 19690720:
                print("Found it: ", 100 * noun + verb)
                break