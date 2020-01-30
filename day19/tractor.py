# Using Eric Wastl's solution to approximate the coord (his has a variable margin of error)
# and then using fitting algorithm to find precise solution by backing up a bit by the margin of error

from opcodes import Processor, get_program
import sys

MARGIN_OF_ERROR = 11

class TractorBeam():
    def __init__(self, input):
        self.program = get_program(input)

    def check_for_pull(self, x, y):
        proc = Processor(self.program, 1024)
        proc.set_std_input([y, x])
        return proc.run_to_output()

def part1(tractor):
    affected = 0
    for y in range(50):
        for x in range(50):
            affected += tractor.check_for_pull(x,y)
    return affected


def get_beam_slopes(tractor, size):
    y = size * 5
    x = round(y / 2)
    while not tractor.check_for_pull(x, y):
        x += 1
    x1 = x
    while tractor.check_for_pull(x, y):
        x += 1
    x2 = x
    return y / x2, y / x1

def approximate_corner(outer_slope, inner_slope, size):
    inner_x = ((outer_slope * size) + size) / (inner_slope - outer_slope)
    return round(inner_x), round((inner_slope * inner_x))


def find_square_origin(tractor, size):
    size -= 1
    outer_slope, inner_slope = get_beam_slopes(tractor, size)
    approx_x, approx_y = approximate_corner(outer_slope, inner_slope, size)

    y = approx_y - round(MARGIN_OF_ERROR * inner_slope)
    upper_limit = approx_y + round(MARGIN_OF_ERROR * inner_slope)
    while y < upper_limit:
        x = approx_x - MARGIN_OF_ERROR
        while not tractor.check_for_pull(x,y): x += 1
        if tractor.check_for_pull(x, y - size) and tractor.check_for_pull(x + size, y - size):
            return x, y - size
        y += 1

def part2(tractor):
    x,y = find_square_origin(tractor, 100)
    return x * 10000 + y

if __name__ == '__main__':
    input = "input.txt"
    if len(sys.argv) > 1: input = sys.argv[1]
    tractor = TractorBeam(input)
    print("Part 1: ", part1(tractor))
    print("Part 2: ", part2(tractor))
