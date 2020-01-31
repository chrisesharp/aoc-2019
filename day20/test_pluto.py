import unittest
from pluto import Maze

class PlutoMazeTest(unittest.TestCase):
  def test_parsing(self):
      input = """         A           
         A           
  #######.#########  
  #######.........#  
  #######.#######.#  
  #######.#######.#  
  #######.#######.#  
  #####  B    ###.#  
BC...##  C    ###.#  
  ##.##       ###.#  
  ##...DE  F  ###.#  
  #####    G  ###.#  
  #########.#####.#  
DE..#######...###.#  
  #.#########.###.#  
FG..#########.....#  
  ###########.#####  
             Z       
             Z       """
      maze = Maze(input.split("\n"))
      self.assertEqual(set(maze.portals.keys()), {(9,2),(9,6),(2,8),(6,10),(2,13),(2,15),(11,12),(13,16)})
      self.assertEqual(set(maze.gate_locs["AA"]),{(9,2)})
      self.assertEqual(set(maze.gate_locs["BC"]),{(9,6),(2,8)})
      self.assertEqual(set(maze.gate_locs["DE"]),{(6,10),(2,13)})
      self.assertEqual(set(maze.gate_locs["FG"]),{(2,15),(11,12)})
      self.assertEqual(set(maze.gate_locs["ZZ"]),{(13,16)})

  def test_next_steps(self):
      input = """         A           
         A           
  #######.#########  
  #######.........#  
  #######.#######.#  
  #######.#######.#  
  #######.#######.#  
  #####  B    ###.#  
BC...##  C    ###.#  
  ##.##       ###.#  
  ##...DE  F  ###.#  
  #####    G  ###.#  
  #########.#####.#  
DE..#######...###.#  
  #.#########.###.#  
FG..#########.....#  
  ###########.#####  
             Z       
             Z       """
      maze = Maze(input.split("\n"))
      next = maze.reachable_gates((9,2)) # AA
      self.assertEqual(set(next), {
        (5, (2, 8), 0), # BC
        (0, (9, 2), 0), # AA
        (2, (9, 2), 0), # AA
        (26,(13,16),0), # ZZ
        (31,(2, 15),0), # FG
        })
      next = maze.reachable_gates((2,8)) # BC
      self.assertEqual(set(next), {
        (1, (9,  6), 0), # BC
        (3, (9,  6), 0), # BC
        (7, (2, 13), 0), # DE
        })

  def test_shortest_path(self):
      input = """         A           
         A           
  #######.#########  
  #######.........#  
  #######.#######.#  
  #######.#######.#  
  #######.#######.#  
  #####  B    ###.#  
BC...##  C    ###.#  
  ##.##       ###.#  
  ##...DE  F  ###.#  
  #####    G  ###.#  
  #########.#####.#  
DE..#######...###.#  
  #.#########.###.#  
FG..#########.....#  
  ###########.#####  
             Z       
             Z       """
      maze = Maze(input.split("\n"))
      path = maze.find_shortest_path()
      self.assertEqual(path, 23)

  def test_next_steps_pt2(self):
    input = """         A           
         A           
  #######.#########  
  #######.........#  
  #######.#######.#  
  #######.#######.#  
  #######.#######.#  
  #####  B    ###.#  
BC...##  C    ###.#  
  ##.##       ###.#  
  ##...DE  F  ###.#  
  #####    G  ###.#  
  #########.#####.#  
DE..#######...###.#  
  #.#########.###.#  
FG..#########.....#  
  ###########.#####  
             Z       
             Z       """
    maze = Maze(input.split("\n"))
    next = maze.reachable_gates((9,2),1) # AA
    self.assertEqual(set(next), {
      (0, (9, 2), 1), # AA
      (2, (9, 2), 1), # AA
      (5, (2, 8), 2), # BC
      (26,(13,16),1), # ZZ
      (31,(2, 15),2), # FG
      })
    next = maze.reachable_gates((2,8),1) # BC
    self.assertEqual(set(next), {
      (7, (2, 13), 2), # DE
      })
    next = maze.reachable_gates((9,6),2) # BC
    self.assertEqual(set(next), {
      (1, (2, 8), 3), # BC
      (3, (2, 8), 3), # BC
      (33,(2, 15),3), # FG
      })


  def test_shortest_path_pt2(self):
      input = """         A           
         A           
  #######.#########  
  #######.........#  
  #######.#######.#  
  #######.#######.#  
  #######.#######.#  
  #####  B    ###.#  
BC...##  C    ###.#  
  ##.##       ###..HI  
  ##...DE  F  ###.#  
  #####    G  ###.#  
  #....HI #.#####.#  
DE..#######...###.#  
  #.#########.###.#  
FG..#########.....#  
  ###########.#####  
             Z       
             Z       """
      maze = Maze(input.split("\n"))
      path = maze.find_shortest_path(1)
      self.assertEqual(path, 26)
      next = maze.reachable_gates((9,2),1) # AA
      self.assertEqual(set(next), {
        (0, (9, 2), 1), # AA
        (2, (9, 2), 1), # AA
        (5, (2, 8), 2), # BC
        (26,(13,16),1), # ZZ
        (31,(2, 15),2), # FG
        })
    
  def test_shortest_path_pt2(self):
      input =  open("input2.txt").readlines()
      maze = Maze(input)
      self.assertTrue(maze.is_outer_gate((19,2)))
      self.assertTrue(maze.is_outer_gate((2,15)))
      self.assertTrue(maze.is_outer_gate((15,34)))
      self.assertTrue(maze.is_outer_gate((42,25)))
      path = maze.find_shortest_path(1)
      self.assertEqual(path, 396)

    
if __name__ == '__main__':
    unittest.main()


