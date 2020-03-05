from math import floor

def fuel_calc(mass):
    return max(0, floor(mass / 3) - 2)

def fuel_calc2(mass):
    extra_fuel = fuel_calc(mass)
    fuel_mass = extra_fuel
    while fuel_mass > 2:
        fuel_mass = fuel_calc(fuel_mass)
        extra_fuel += fuel_mass
    return extra_fuel



if __name__ == '__main__':
    file = open("input.txt", "r")
    total = 0
    for line in file:
        total += fuel_calc2(int(line))
    print("total:", total)