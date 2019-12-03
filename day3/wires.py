from sys import maxsize

deltas = {
    "U": (0,1),
    "R": (1,0),
    "D": (0,-1),
    "L": (-1,0)
}

def trace_path(route):
    x,y = (0,0)
    dx,dy = (0,0)
    path = []
    for step in route.split(','):
        dx, dy = deltas[step[0]]
        for i in range(int(step[1:])):
            x += dx
            y += dy
            path.append((x,y))
    return path

def manhatten_distance(A,B):
    (x,y) = A
    (p,q) = B
    return abs(x-p) + abs(y-q)

def distance(A, paths=None):
    return manhatten_distance(A, (0,0))

def stepcount(point, paths):
    steps = 0
    for path in paths:
        steps += path.index(point) + 1
    return steps

def calculate_distance(func, paths):
    intersect = set(paths[0]) & set(paths[1])
    steps = maxsize
    for point in intersect:
        steps = min(steps, func(point, paths))
    return steps

if __name__ == '__main__':
    file = open("input1.txt", "r")
    first = trace_path(file.readline())
    second = trace_path(file.readline())
    result = calculate_distance(distance, [first, second])
    print("Part 1:", result)
    result = calculate_distance(stepcount, [first, second] )
    print("Part 2:", result)
