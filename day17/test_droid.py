import unittest
from opcodes import Processor
from droid import factorize
from direction import Direction

class DroidTest(unittest.TestCase):    
    def test_factoring_funcs_1(self):
        path = ["L","1","L","1","R","2","L","1","L","1","R","2","L","1","L","1","R","2"]
        funcs, path = factorize(path)
        print(funcs)
        self.assertEqual(funcs, ["L,1,L,1,R,2"])
    
    def test_factoring_funcs_2(self):
        path = ["L","1","L","1","R","2","R","3","L","1","R","2","L","1","L","1","R","2"]
        funcs, path = factorize(path)
        self.assertTrue("L,1,L,1,R,2" in funcs)
        self.assertTrue("R,3,L,1,R,2" in funcs)
