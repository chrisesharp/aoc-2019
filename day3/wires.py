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

def distance(A,B):
    (x,y) = A
    (p,q) = B
    return abs(x-p) + abs(y-q)

def closest(intersect):
    closest = maxsize
    for point in intersect:
        dist = distance(point,(0,0))
        closest = min(closest, dist)
    return closest

def stepcount(point, path):
    steps = 0
    for step in path:
        steps += 1
        if step == point:
            break
    return steps


def shortest(intersect, paths):
    closest = maxsize
    for point in intersect:
        steps = 0
        for path in paths:
            steps += stepcount(point, path)
        closest = min(steps, closest)
    return closest


if __name__ == '__main__':
    file = open("input1.txt", "r")
    first = trace_path(file.readline())
    second = trace_path(file.readline())
    intersect = set(first) & set(second)
    result = closest(intersect)
    print("Part 1:", result)
    result = shortest(intersect,[first,second])
    print("Part 2:", result)

