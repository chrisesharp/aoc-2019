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

def part1(instructions, noun, verb):
    prog = program(instructions, noun, verb)
    return run(prog)[0]

def part2(instructions):
    for noun in range(100):
        for verb in range(100):
            if part1(instructions, noun, verb) == 19690720:
                return 100 * noun + verb

if __name__ == '__main__':
    prog = open("input.txt").read()
    instructions = [int(x) for x in prog.split(",")]
    noun = 12
    verb = 2
    print("Part 1:", part1(instructions, noun, verb))
    print("Part 2:", part2(instructions))
