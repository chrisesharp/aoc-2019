import unittest

from wires import trace_path, distance, closest, shortest, stepcount

class TestTest(unittest.TestCase):
    def test_trace_path1(self):
        input = "R1,D2,L3,U4"
        path = set(trace_path(input))
        expected = set([(1,0),(1,-1),(1,-2),(0,-2),(-1,-2),(-2,-2),(-2,-1),(-2,0),(-2,1),(-2,2)])
        self.assertEqual(expected, path)

    def test_trace_path2(self):
        input = "R2,D2,L2,U2"
        path = set(trace_path(input))
        expected = set([(1,0),(2,0),(2,-1),(2,-2),(1,-2),(0,-2),(0,-1),(0,0)])
        self.assertEqual(expected, path)
    
    def test_first_example(self):
        first = trace_path("R8,U5,L5,D3")
        second = trace_path("U7,R6,D4,L4")
        intersect = set(first) & set(second)
        result = closest(intersect)
        self.assertEqual(6, result)
    
    def test_second_example(self):
        first = trace_path("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51")
        second = trace_path("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")
        intersect = set(first) & set(second)
        result = closest(intersect)
        self.assertEqual(135, result)
    
    def test_step_count(self):
        first = trace_path("R2,D2,L2,U2")
        intersect = (2,-2)
        steps = stepcount(intersect, first)
        self.assertEqual(4,steps)
    
    def test_shortest(self):
        first = trace_path("R8,U5,L5,D3")
        second = trace_path("U7,R6,D4,L4")
        intersect = set(first) & set(second)
        steps = shortest(intersect, [first, second])
        self.assertEqual(30,steps)

    
    def test_third_example(self):
        first = trace_path("R75,D30,R83,U83,L12,D49,R71,U7,L72")
        second = trace_path("U62,R66,U55,R34,D71,R55,D58,R83")
        intersect = set(first) & set(second)
        result = shortest(intersect, [first, second])
        self.assertEqual(610, result)

    def test_fourth_example(self):
        first = trace_path("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51")
        second = trace_path("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")
        intersect = set(first) & set(second)
        result = shortest(intersect, [first, second])
        self.assertEqual(410, result)
        

if __name__ == '__main__':
    unittest.main()