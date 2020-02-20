import unittest
from shuffle import shuffle, new_stack, cut, increment

class ShuffleTest(unittest.TestCase):
  def test_cut_positive(self):
    stack = [0,1,2,3,4,5,6,7,8,9]
    self.assertEqual([3,4,5,6,7,8,9,0,1,2],cut(stack,3))
  
  def test_cut_negative(self):
    stack = [0,1,2,3,4,5,6,7,8,9]
    self.assertEqual([6,7,8,9,0,1,2,3,4,5],cut(stack,-4))
  
  def test_new_stack(self):
    stack = [0,1,2,3,4,5,6,7,8,9]
    self.assertEqual([9,8,7,6,5,4,3,2,1,0],new_stack(stack))

  def test_increment(self):
    stack = [0,1,2,3,4,5,6,7,8,9]
    self.assertEqual([0,7,4,1,8,5,2,9,6,3],increment(stack,3))

  def test_parsing(self):
    input = """deal with increment 7
deal into new stack
deal into new stack
"""
    stack = [0,1,2,3,4,5,6,7,8,9]
    stack = shuffle(input, stack)
    self.assertEqual([0,3,6,9,2,5,8,1,4,7],stack)

  def test_ex2(self):
    input = """cut 6
deal with increment 7
deal into new stack
"""
    stack = [0,1,2,3,4,5,6,7,8,9]
    stack = shuffle(input, stack)
    self.assertEqual([3,0,7,4,1,8,5,2,9,6],stack)
  
  def test_ex3(self):
    input = """deal with increment 7
deal with increment 9
cut -2
"""
    stack = [0,1,2,3,4,5,6,7,8,9]
    stack = shuffle(input, stack)
    self.assertEqual([6,3,0,7,4,1,8,5,2,9],stack)
  
  def test_ex4(self):
    input = """deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1
"""
    stack = [0,1,2,3,4,5,6,7,8,9]
    stack = shuffle(input, stack)
    self.assertEqual([9,2,5,8,1,4,7,0,3,6],stack)
  
  def test_find_card(self):
    stack = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
    stack = new_stack(stack)
    self.assertEqual(12,stack.index(1))

if __name__ == '__main__':
    unittest.main()
