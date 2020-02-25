import time

icons = { True:"#", False:"." }

class GameOfLife(object):
    def __init__(self, input):
        (self.max_x, self.max_y, alive_cells) = parse(input)
        self.all_cells = [(x,y) for y in range(self.max_y) for x in range(self.max_x)]
        self.cells = self.serialize(alive_cells)
        self.patterns = set([int(self.cells[-1::-1],2)])
    
    def __str__(self):
        return self.print(0)
        
    def tick(self):
        self.cells = self.serialize(self.next_gen())
        layout_id = int(self.cells[-1::-1],2)
        if layout_id in self.patterns:
            return layout_id
        self.patterns.add(layout_id)
    
    def next_gen(self):
        return self.survivors().union(self.births())
    
    def serialize(self, cells):
        return "".join([str(int(cell in cells)) for cell in self.all_cells])

    def deserialize(self, cells):
        tmp = list(cells)
        return set([cell for cell in self.all_cells if int(tmp.pop(0))])
        
    def survivors(self):
        cells = self.deserialize(self.cells)
        return set([cell for cell in cells if len(self.liveNeighbours(cell)) == 1 ])
    
    def births(self):
        cells = self.deserialize(self.cells)
        return set([deadNeighbour for cell in cells for deadNeighbour in self.deadNeighbours(cell) if len(self.liveNeighbours(deadNeighbour)) in [1, 2]])
    
    def neighbourhood(self, cell):
        deltas = [ (-1, 0), (0,-1), (1, 0), (0, 1) ]
        x, y = cell
        return [(x+dx, y+dy) for (dx, dy) in deltas]

    def neighbours(self, cell, alive):
        cells = self.deserialize(self.cells)
        return set([neighbour for neighbour in self.neighbourhood(cell) if (neighbour in cells) is alive])

    def liveNeighbours(self, cell):
        return self.neighbours(cell, True)
    
    def deadNeighbours(self, cell):
        return self.neighbours(cell, False)

    def print(self, level):
        alive_cells = self.deserialize(self.cells)
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
            if char == "#":
                cells.update([(x,y)])
            x += 1
        x = 0
        y += 1
    return cells


if __name__ == "__main__":
    input = open("input.txt").read()
    game = GameOfLife(input)
    id=False
    while not id:
        id = game.tick()
    print("Part 1:",id)