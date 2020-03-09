from enum import Enum

class Tile(Enum):
    EMPTY = 0
    WALL  = 1
    BLOCK = 2
    PADDLE= 3
    BALL  = 4

    def __str__(self):
        return tile_map.get(self)
    
tile_map = {
    Tile.EMPTY  : " ",
    Tile.WALL   : "#",
    Tile.BLOCK  : "=",
    Tile.PADDLE : "-",
    Tile.BALL   : "o"
}