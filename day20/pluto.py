import itertools
import heapq
import collections

above = lambda loc: (loc[0], loc[1]-1)
below = lambda loc: (loc[0], loc[1]+1)
left  = lambda loc: (loc[0]-1, loc[1])
right = lambda loc: (loc[0]+1, loc[1])

class Maze():
    def __init__(self, input, part2=False):
        self.grid = [s for s in input]
        self.width, self.height = len(self.grid[0]), len(self.grid)
        self.portals = {}
        self.gate_locs = collections.defaultdict(list)

        def find_gate(loc, direction, opposite):
            label = gate_loc = None
            if self.at(direction(loc)).isupper():
                label = self.at(loc) + self.at(direction(loc))
                if self.at(opposite(loc)) == '.':
                    gate_loc = opposite(loc)
                elif self.at(direction(direction(loc))) == '.':
                    gate_loc = direction(direction(loc))
            return label, gate_loc


        for loc in [(x,y) for y in range(self.height - 1) for x in range(self.width - 1)]:
            if not self.at(loc).isupper():
                continue
            label, gate_loc = find_gate(loc, below, above)
            if not label:
                label, gate_loc = find_gate(loc, right, left)
            if label:
                self.gate_locs[label].append(gate_loc)
                self.portals[gate_loc] = label

        self.width -= 1
        self.start = list(self.gate_locs["AA"]).pop()
        self.end = list(self.gate_locs["ZZ"]).pop()
        while self.optimazing():
            pass
    
    def at(self, loc):
        x,y = loc
        if 0 <= y < self.height and 0 <= x <= self.width:
            return self.grid[y][x]
    
    def find_shortest_path(self, level=0):
        queue = [(0, level, self.start)]
        seen = set()
        while queue:
            dist, level, current_position = heapq.heappop(queue)
            if current_position == self.end and level <= 1: return dist
            if (current_position, level) in seen: continue
            seen.add((current_position, level))
            for length, pos, new_level in self.reachable_gates(current_position, level):
                heapq.heappush(queue, (dist + length, new_level, pos))

    def reachable_gates(self, loc, level=0):
        queue = collections.deque([(loc, 0)])
        seen = set()
        while queue:
            current, length = queue.popleft()
            portal = self.portals.get(current)
            if portal:
                gates = list(self.gate_locs[portal])
                if len(gates) > 1:
                    gates.remove(current)
                    gate = gates[0]
                    if not level: yield (length + 1, gate, 0)
                    elif not self.is_outer_gate(current):
                        yield (length + 1, gate, level + 1 )
                    elif level > 1:
                        yield (length + 1, gate, level - 1 )
                else:
                    if level <= 1: yield (length, current, level)

            for neighbour, tile in self.get_adjacents(current):
                if neighbour in seen: continue
                seen.add(neighbour)
                if tile == ".": queue.append((neighbour, length + 1))

    def is_outer_gate(self, loc):
        return (loc[0]==2 or loc[0]==self.width - 3) or (loc[1]==2 or loc[1]==self.height - 3)
    
    def get_adjacents(self, loc):
        deltas = [above(loc), below(loc),left(loc),right(loc)]
        for loc in deltas:
            tile = self.at(loc)
            if tile != "#": yield loc, tile
    
    def gate_letters(self, pos):
        neighbours = []
        gate = None
        for loc, tile in self.get_adjacents(pos):
            if tile == ".":
                gate = loc
            elif tile and tile.isupper():
                neighbours.append(tile)
        return neighbours, gate
    
    def optimazing(self):
        altered = 0
        for y in range(self.height-1):
            for x in range(self.width):
                tiles =  [tile for loc, tile in self.get_adjacents((x, y))]
                if self.grid[y][x] == "." and tiles.count("#") == 3:
                    line = self.grid[y]
                    self.grid[y] = line[:x] + "#" + line[x+1:]
                    altered += 1
        return altered

if __name__ == "__main__":
    input = open("input.txt").readlines()
    maze = Maze(input)
    steps = maze.find_shortest_path()
    print("Part 1: ", steps)
    steps = maze.find_shortest_path(1)
    print("Part 2: ", steps)
    