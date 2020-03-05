class Planet():
    def __init__(self, name, orbits):
        self.name = name
        self.orbits = orbits
        self.satellites = []

    def total_orbits(self):
        if self.orbits == None:
            return 0
        return 1 + self.orbits.total_orbits()

class StarMap():

    def __init__(self, file):
        self.planets = []

        for line in file:
            orbited, moon = line.strip().split(")")
            planet, satellite = self.find_planets(orbited, moon)
            satellite.orbits = planet
            planet.satellites.append(satellite)
        
    def find_planets(self, orbited, moon):
        planet = None
        satellite = None
        for p in self.planets:
            if p.name == moon:
                satellite = p
            elif p.name == orbited:
                planet = p
        
        if not planet:
            planet = Planet(orbited, None)
            self.planets.append(planet)        
        if not satellite:
            satellite = Planet(moon, planet)
            self.planets.append(satellite)
        return planet, satellite
    
    def find_planet(self, name):
        return [p for p in self.planets if p.name == name][0]
    
    def find_path(self, start, end):
        start = self.find_planet(start)
        searched = [start]
        queue = [start]
        path = []
        while len(queue) > 0:
            planet = queue.pop()
            if not planet:
                continue

            while len(path) > 0:
                if planet not in path[-1].satellites and planet != path[-1].orbits:
                    path.pop()
                else:
                    break

            if len(planet.satellites) > 0:
                path.append(planet)

            if end in [s.name for s in planet.satellites]:
                break

            if planet.orbits not in searched:
                queue.append(planet.orbits)
                searched.append(planet.orbits)
            
            for satellite in planet.satellites:
                if satellite not in searched:
                    queue.append(satellite)
                    searched.append(satellite)
        return path

if __name__ == '__main__':
    file = open("input.txt").readlines()
    starmap = StarMap(file)
    
    count = 0
    for planet in starmap.planets:
        count += planet.total_orbits()
    print("Part1:",count)

    path = starmap.find_path("YOU", "SAN")
    print("Part2:",len(path) - 1)