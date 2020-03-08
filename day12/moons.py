class Moon():
    def __init__(self, input):
        x,y,z = [0, 0, 0]
        for element in input[1:-1].split(","):
            element = element.strip()
            if element[0] == "x":
                x = int(element[2:])
            elif element[0] == "y":
                y = int(element[2:])
            else:
                z = int(element[2:])
        self.pos = [x, y, z]
        self.orig = [x, y, z]
        self.velocity = [0, 0, 0]
    
    def __repr__(self):
        return tuple(self.pos)

    def tick(self):
        for i in range(3):
            self.tick_axis(i)
    
    def tick_axis(self, i):
        self.pos[i] += self.velocity[i]
    
    def energy(self):
        x,y,z = self.pos
        potential = abs(x) + abs(y) + abs(z)
        x,y,z = self.velocity
        kinetic = abs(x) + abs(y) + abs(z)
        return potential * kinetic
    
    def at_start(self, i):
        return self.orig[i] == self.pos[i] and self.velocity[i] == 0


def get_moons(input):
    moons = []
    for line in input.split("\n"):
        moons.append(Moon(line))
    return moons

def get_pairs(input):
    moons = input[:]
    pairs = []
    while moons:
        moon = moons.pop(0)
        for other_moon in filter(lambda a: a != moon, moons) :
            pairs.append([moon, other_moon])
    return pairs

def apply_gravity(pair):
    for i in range(3):
        apply_gravity_by_axis(pair, i)
    return pair

def apply_gravity_by_axis(pair, axis):
    sign = lambda x: x and (1, -1)[x < 0]
    A, B = pair
    a = A.pos[axis]
    b = B.pos[axis]
    delta = sign(b-a)
    A.velocity[axis] += delta
    B.velocity[axis] -= delta
    return A,B

def tick(moons):
    energy = 0
    for pair in get_pairs(moons):
        apply_gravity(pair)
    
    for moon in moons:
        moon.tick()
        energy += moon.energy()
    return energy

def tick_cycles(moons):
    at_start = False
    times = [0,0,0]
    for axis in range(3):
        while not at_start:
            for pair in get_pairs(moons):
                apply_gravity_by_axis(pair, axis)
            for moon in moons:
                moon.tick_axis(axis)
            times[axis] += 1
            at_start = (moons[0].at_start(axis) and 
                        moons[1].at_start(axis) and
                        moons[2].at_start(axis) and
                        moons[3].at_start(axis))
        at_start = False
    return times

def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def lcm(x, y):
   return (x*y)//gcd(x,y)


if __name__ == '__main__':
    input = open("input.txt").read()
    moons = get_moons(input)
    for i in range(1000):
        energy = tick(moons)
    print("Part 1: ",energy)

    moons = get_moons(input)
    tx, ty, tz = tick_cycles(moons)
    cycle = lcm(lcm(tx, ty), lcm(ty, tz))
    print("Part 2: ", cycle )

    