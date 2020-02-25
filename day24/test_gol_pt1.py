from gol_pt1 import GameOfLife, parse
    
def test_parsing_1_cell():
    input = "#\n"
    alive_cells = set()
    (max_x, max_y, alive_cells) = parse(input)
    assert max_x == 1
    assert max_y == 1
    assert alive_cells == {(0,0)}
    
def test_ex_one():
    input = """....#
#..#.
#..##
..#..
#....
"""
    game = GameOfLife(input)
    game.tick()
    print(game.print(0))
    assert game.print(0) == """#..#.
####.
###.#
##.##
.##..
"""
    game.tick()
    print(game.print(0))
    assert game.print(0) == """#####
....#
....#
...#.
#.###
"""
    game.tick()
    print(game.print(0))
    assert game.print(0) == """#....
####.
...##
#.##.
.##.#
"""
    game.tick()
    print(game.print(0))
    assert game.print(0) == """####.
....#
##..#
.....
##...
"""
