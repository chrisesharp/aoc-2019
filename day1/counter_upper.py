from math import floor

def fuel_calc(mass):
    return floor(mass / 3) - 2

def fuel_calc2(mass):
    extra_fuel = fuel_calc(mass)
    fuel_mass = extra_fuel
    while fuel_mass > 2:
        fuel_mass = max(fuel_calc(fuel_mass),0)
        extra_fuel += fuel_mass
    return extra_fuel



if __name__ == '__main__':
    file = open("input1.txt", "r")
    total = 0
    for line in file:
        total += fuel_calc2(int(line))
    print("total:", total)