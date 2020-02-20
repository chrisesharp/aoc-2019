from opcodes import Processor, get_program
import sys

class SpringDroid():
    def __init__(self, input):
        self.program = get_program(input)
    
    def run_script(self, input):
        result = []
        proc = Processor(self.program, 1024)
        script = []
        for c in reversed(input):
            if input:
                script.append(ord(c))
        proc.set_std_input(script)
        while output := proc.run_to_output():
            if output < 255:
                result.append(chr(output))
            else:
                return [output]
        return result[34:]



if __name__ == '__main__':
    input = "input.txt"
    if len(sys.argv) > 1: input = sys.argv[1]
    droid = SpringDroid(input)
    part1 = \
"""NOT A J
NOT C T
AND D T
OR T J
WALK
"""
    output = droid.run_script(part1)
    if len(output) == 1:
        print ("Part 1:",output.pop())
    else:
        print("Part 1: ", "".join(output))
    part2 = \
"""NOT A J
NOT B T
AND H T
OR T J
NOT C T
AND H T
OR T J
AND D J
RUN
"""
    output = droid.run_script(part2)
    if len(output) == 1:
        print ("Part 2:",output.pop())
    else:
        print("Part 2: ", "".join(output))

