import time

left_edge = [(0,0),(0,1),(0,2),(0,3),(0,4)]
right_edge = [(4,0),(4,1),(4,2),(4,3),(4,4)]
top_edge = [(0,0),(1,0),(2,0),(3,0),(4,0)]
bottom_edge = [(0,4),(1,4),(2,4),(3,4),(4,4)]
left_centre = (1,2)
right_centre = (3,2)
top_centre = (2,1)
bottom_centre = (2,3)
centres = [left_centre, top_centre, right_centre, bottom_centre]
all_boundaries = set(left_edge + right_edge + top_edge + bottom_edge + centres)

edge_maps = {
    left_centre : left_edge,
    right_centre : right_edge,
    top_centre : top_edge,
    bottom_centre : bottom_edge
}

icons = { True:"#", False:"." }

class GameOfLife(object):
    def __init__(self, input):
        (self.max_x, self.max_y, alive_cells) = parse(input)
        self.all_cells = [(x,y) for y in range(self.max_y) for x in range(self.max_x)]
        self.levels = { 0: alive_cells}    
    def __str__(self):
        return self.print(0)
    
    def count_bugs(self):
        return sum([len(self.levels[level]) for level in self.levels])
    
    def get_level(self, level):
        if level not in self.levels:
            self.levels[level] = set()
        return self.levels[level]
    
    def tick_all(self, max_mins=1):
        new_levels = {}
        current_levels = [-1, 0, 1]
        time = 0
        while time < max_mins:
            for level in current_levels:
                new_levels[level] = self.next_gen(level)
            self.levels = dict(new_levels)
            time += 1
            current_levels.append(time+1)
            current_levels.append(-(time+1))
    
    def next_gen(self, level):
        return self.survivors(level).union(self.births(level))
        
    def survivors(self, level):
        cells = self.get_level(level)
        return set([cell for cell in cells if self.will_survive(cell, level)])
    
    def births(self, level):
        cells = self.get_level(level)
        births = set()
        for cell in cells:
            for (deadNeighbour, lvl) in self.deadNeighbours(cell, level):
                if lvl == level and self.will_be_born(deadNeighbour, lvl):
                    births.add(deadNeighbour)
        
        for cell in all_boundaries - cells:
            if self.will_be_born(cell, level):
                births.add(cell)
        return births
    
    def will_survive(self, cell, level):
        return len(self.liveNeighbours(cell, level)) == 1

    def will_be_born(self, cell, level):
        return len(self.liveNeighbours(cell, level)) in [1, 2]

    def neighbourhood(self, cell):
        deltas = [ (-1, 0), (0,-1), (1, 0), (0, 1) ]
        x, y = cell
        return [(x+dx, y+dy) for (dx, dy) in deltas if (x+dx, y+dy) != (2,2)]

    def neighbours(self, cell, level, alive):
        cells = self.get_level(level)
        lower_level = self.get_level(level - 1)
        neighbours = []
        
        for centre, edge in edge_maps.items():
            if cell == centre:
                for n in self.other_neighbours(alive, edge_maps[cell], level + 1):
                    neighbours.append(n)
            elif cell in edge and (centre in lower_level) is alive:
                    neighbours.append((centre, level - 1))

        for neighbour in self.neighbourhood(cell):
            if mapped := self.out_of_bounds_map(neighbour):
                if (mapped in lower_level) is alive:
                    neighbours.append((mapped, level - 1))
            elif (neighbour in cells) is alive:
                neighbours.append((neighbour, level))
        return set(neighbours)
    
    def other_neighbours(self, alive, edge, lvl):
        level = self.get_level(lvl)
        return [(neighbour, lvl) for neighbour in edge if (neighbour in level) is alive]

    def out_of_bounds_map(self, cell):
        x, y = cell
        if x == -1:
            return left_centre
        elif x == self.max_x:
            return right_centre
        elif y == -1:
            return top_centre
        elif y == self.max_y:
            return bottom_centre

    def liveNeighbours(self, cell, level):
        return self.neighbours(cell, level, True)
    
    def deadNeighbours(self, cell, level):
        return self.neighbours(cell, level, False)
    
    def print(self, level):
        alive_cells = self.get_level(level)
        output = ""
        for (x,y) in self.all_cells:
            output += icons[(x,y) in alive_cells]
            if x == self.max_x-1: output += "\n"
        return output

def parse(input):
    alive_cells = set()   
    lines = input.splitlines()
    (maxx,maxy) = map(int,[len(lines[0]),len(lines)])
    alive_cells = findCells(lines)          
    return (maxx, maxy, alive_cells)

def findCells(lines):
    cells = set()
    x = y = 0 
    for line in lines:
        for char in line:
            if char == icons[True]:
                cells.update([(x,y)])
            x += 1
        x = 0
        y += 1
    return cells


if __name__ == "__main__":
    input = open("input.txt").read()
    game = GameOfLife(input)
    game.tick_all(200)
    print("Part 2:", game.count_bugs())