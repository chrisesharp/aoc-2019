# This is based on a superb solution by Eric Wastl
# I've just tried to refactor to make it easier to read
# by wrapping the 2D array in an object to avoid having
# to expose the x,y components of a location

from __future__ import print_function, division
import collections
import itertools
import heapq

not_wall = lambda x: x != '#'
not_door = lambda x: not x.isupper()
key_for = lambda x: x.lower()
is_key = lambda x: x.islower()

class Grid():
    def __init__(self, input, part2=False):
        self.grid = [s.rstrip() for s in input]
        self.width, self.height = len(self.grid[0]), len(self.grid)
        one_dimensional_grid = list(itertools.chain.from_iterable(self.grid))
        self.allkeys = set(c for c in one_dimensional_grid if c.islower())

        index = one_dimensional_grid.index('@')
        x, y = index % self.width, index // self.width

        self.start_pos = ((x,y),)
        if part2:
            self.grid[y-1] = self.grid[y-1][:x]   +  '#'  + self.grid[y-1][x+1:]
            self.grid[  y] = self.grid[y  ][:x-1] + '###' + self.grid[y  ][x+2:]
            self.grid[y+1] = self.grid[y+1][:x]   +  '#'  + self.grid[y+1][x+1:]
            self.start_pos = ((x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1), )
    
    def at(self, loc):
        x,y = loc
        return self.grid[y][x]
        
    def reachable_keys(self, loc, keys):
        queue = collections.deque([(loc, 0)])
        seen = set()
        
        while queue:
            current, length = queue.popleft()
            node = self.at(current)
            if is_key(node) and node not in keys:
                yield length, current, node
                continue
            for neighbour in self.get_adjacents(current):
                if neighbour in seen:
                    continue
                seen.add(neighbour)
                node = self.at(neighbour)
                if node and (not_wall(node) and (not_door(node) or key_for(node) in keys)):
                    queue.append((neighbour, length + 1))

    def get_adjacents(self, loc):
        (target_x, target_y) = loc
        deltas = ((target_x, target_y - 1),
                    (target_x - 1, target_y),
                    (target_x, target_y + 1),
                    (target_x + 1, target_y))
        for x,y in deltas:
            if 0 <= x < self.width and 0 <= y < self.height:
                yield (x,y)

def shortest_path(grid):
    pos = grid.start_pos
    queue = [(0, pos, frozenset())]
    seen = set()
    while queue:
        dist, current_pos, keys = heapq.heappop(queue)
        if keys == grid.allkeys:
            return dist

        if (current_pos, keys) in seen:
            continue
        seen.add((current_pos, keys))

        for i, bot in enumerate(current_pos):
            for length, pos, key in grid.reachable_keys(bot, keys):
                next_pos = current_pos[0:i] + (pos,) + current_pos[i+1:]
                heapq.heappush(queue, (dist + length, next_pos, keys | frozenset([key])))
    return None


if __name__ == "__main__":
    input = open("input.txt").readlines()
    print("Part 1:")
    print(shortest_path(Grid(input)))
    
    print("Part 2:")
    print(shortest_path(Grid(input, True)))
