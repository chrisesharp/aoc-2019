import math

def get_map(input):
    x,y = 0,0
    starmap = set()
    for y, line in enumerate(input.split()):
        for x, space in enumerate(line.rstrip()):
            if (space != "."):
                starmap.add((x,y))
    return starmap

def angle(A, B):
    result = math.atan2(B[0] - A[0], A[1] - B[1]) * 180 / math.pi
    return (360 + result) % 360

def num_visible(A, starmap):
    unique_angles = set()
    for asteroid in [asteroid for asteroid in starmap if asteroid != A]:
        unique_angles.add(angle(A,asteroid))
    return len(unique_angles)

def best_location(starmap):
    count_map = {}
    for asteroid in starmap:
        count_map[asteroid] = num_visible(asteroid, starmap)
    return [(k, count_map[k]) for k in sorted(count_map, key=count_map.get, reverse=True)][0]

def distance(A, B):
    return abs(A[0] - B[0]) + abs(A[1] - B[1])

def get_angles(laser, starmap):
    return sorted(
                ((angle(laser, target), target) for target in starmap if target != laser),
                key=lambda entry: (entry[0], distance(laser, entry[1]))
            )

def find_nth_target(n, laser, starmap):
    angles = get_angles(laser, starmap)
    idx = 0
    target_angle, target = angles.pop(idx)
    count = 1

    while count < n and angles:
        if target_angle == angles[idx][0]:
            idx += 1
            if idx >= len(angles):
                idx = 0
            continue
        target_angle, target = angles.pop(idx)
        count += 1
    return target

if __name__ == '__main__':
    input = open("input.txt").read()
    print("Parsing map")
    starmap = get_map(input)

    print("Part 1:")
    best = best_location(starmap)
    print("Location: {}, visible:{}".format(*best))

    print("Part 2")
    laser = best[0]
    asteroid = find_nth_target(200, laser, starmap)
    print("Answer: ", asteroid[0]*100 + asteroid[1])