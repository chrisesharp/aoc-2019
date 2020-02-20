def new_stack(stack):
    return stack[::-1]

def increment(stack, point):
    i=0
    new_stack=[0]*len(stack)
    while stack:
        new_stack[i]=stack.pop(0)
        i = (i+point)%len(new_stack)
    return new_stack

def cut(stack, point):
    return stack[point:] + stack[:point]

def shuffle(input, stack):
    for line in input.strip().split("\n"):
        if line.find("new stack") >= 0:
            stack = new_stack(stack)
        elif line.find("increment") >= 0:
            point = int(line.split()[3])
            stack = increment(stack, point)
        elif line.find("cut") >= 0:
            point = int(line.split()[1])
            stack = cut(stack, point)
    return stack

def create_deck(size):
    stack = [0]*size
    for i in range(size):
        stack[i] = i
    return stack

def play(input):
    n = 10007
    times = 1
    stack = create_deck(n)
    for i in range(times):
        stack = shuffle(input, stack)
    return stack


if __name__ == "__main__":
    input = open("input.txt").read()
    stack = play(input)
    print("Part 1: ", stack.index(2019))
    print("Part 2 is a maths problem, not a programming problem! See foo2.py")
