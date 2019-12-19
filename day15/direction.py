from enum import IntEnum

class Direction(IntEnum):
    EAST = 3
    NORTH = 1
    WEST = 4
    SOUTH = 2

def opposite_direction(direction):
    return {
            Direction.NORTH : Direction.SOUTH, 
            Direction.SOUTH : Direction.NORTH, 
            Direction.WEST : Direction.EAST, 
            Direction.EAST : Direction.WEST
            }[direction]


def next_location(coords, direction):
    return {
        Direction.WEST: lambda coords: ((coords[0] - 1),
                                        coords[1]),
        Direction.EAST: lambda coords: ((coords[0] + 1),
                                         coords[1]),
        Direction.NORTH: lambda coords: (coords[0],
                                      (coords[1] - 1)),
        Direction.SOUTH: lambda coords: (coords[0],
                                        (coords[1] + 1))
        }[direction](coords)