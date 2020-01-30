import unittest
from tractor import TractorBeam, part1, part2

class TractorBeamTest(unittest.TestCase):
    def test_tractor_program(self):
        tractor = TractorBeam("input.txt")
        x,y = 0,0
        output = tractor.check_for_pull(x, y)
        self.assertEqual(output, 1)
    
    def test_2(self):
        tractor = TractorBeam("input2.txt")
        self.assertEqual(114, part1(tractor))
        self.assertEqual(10671712, part2(tractor))
    
    def test_3(self):
        tractor = TractorBeam("input3.txt")
        self.assertEqual(131, part1(tractor))
        self.assertEqual(15231022, part2(tractor))
    
    def test_4(self):
        tractor = TractorBeam("input4.txt")
        self.assertEqual(211, part1(tractor))
        self.assertEqual(8071006, part2(tractor))
    
    def test_final_solution(self):
        tractor = TractorBeam("input.txt")
        self.assertEqual(160, part1(tractor))
        self.assertEqual(9441282, part2(tractor))


if __name__ == '__main__':
    unittest.main()


