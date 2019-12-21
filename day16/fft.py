from itertools import cycle, accumulate

def apply_fft(input, length=8):
    base_pattern = [0, 1, 0, -1]
    output = [] 
    digits = [int(i) for i in input]
    for i in range(len(digits)):
        pattern = pattern_cycle(base_pattern, i)
        patt = [next(pattern) for _ in range(length)]
        new_digit= sum(map(lambda v: v[0]*v[1], zip(digits, patt)))
        output.append(str(abs(new_digit)%10))
    return ''.join(output)

def part1(input):
    part1 = input[:]
    length = len(str(input))
    for _ in range(100):
        part1 = apply_fft(part1, length)
    return int(str(part1)[:8])

def part2(input):
    offset = int(input[:7])
    digits = [int(i) for i in input]
    digit = cycle(reversed(digits))
    arr = [next(digit) for _ in range(10000 * len(digits) - offset)]
    for _ in range(100):
        arr = [n % 10 for n in accumulate(arr)]
    return ''.join(list(map(str,arr[-1:-9:-1])))

def pattern_cycle(pattern, index):
    cyc = cycle(calc_pattern(pattern, index))
    next(cyc)
    return cyc

def calc_pattern(pattern, index):
    return [x for x in pattern for _ in range(index+1)]

if __name__ == '__main__':
    input = open("input.txt").readline().strip()
    part1 = input[:]
    length = len(str(input))
    for _ in range(100):
        part1 = apply_fft(part1, length)
    output = int(str(part1)[:8])
    print("Part 1:",output)
    print("Part 2:",part2(input))