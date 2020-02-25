from gol import GameOfLife, parse

def test_neighbours_pt2():
    input = """#.#.#
.###.
##.##
.###.
#.#.#
"""
    
    game = GameOfLife(input)
    neighbours = game.neighbours((3,2),-1,True)
    assert neighbours == {((4, 0), 0), ((4, 2), 0), ((4, 4), 0)}

    neighbours = game.neighbours((1,2),-1,True)
    assert neighbours == {((0, 0), 0), ((0, 2), 0), ((0, 4), 0)}

    neighbours = game.neighbours((4,0),1,True)
    assert neighbours == {((2, 1), 0), ((3, 2), 0)}

    assert len(game.births(0)) == 0
    assert len(game.births(1)) == 16

def test_neighbours_pt2_2():
    input = """..#..
.###.
##.##
.###.
..#..
"""
    
    game = GameOfLife(input)
    assert len(game.births(-1)) == 4

def test_part2():
    input = """....#
#..#.
#..##
..#..
#....
"""
    game = GameOfLife(input)
    game.tick_all(10)
    print(game.print(-1))
    print(game.print(0))
    print(game.print(1))
    assert game.print(0) == """.#...
.#.##
.#...
.....
.....
"""
    assert game.print(-1) == """#..##
...##
.....
...#.
.####
"""
    assert game.print(1) == """.##..
#..##
....#
##.##
#####
"""

    assert game.print(5) == """####.
#..#.
#..#.
####.
.....
"""

    assert game.print(-5) == """..#..
.#.#.
....#
.#.#.
..#..
"""
    assert game.count_bugs() == 99