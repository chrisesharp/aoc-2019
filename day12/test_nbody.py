import unittest

from moons import Moon, get_moons, get_pairs, apply_gravity, tick, tick_cycles, lcm

class MoonTest(unittest.TestCase):    
    def test_parse_input(self):
        input = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""
        moons = get_moons(input)
        self.assertEqual((-1,0,2),moons[0].__repr__())
        self.assertEqual((2,-10,-7),moons[1].__repr__())
        self.assertEqual((4,-8,8),moons[2].__repr__())
        self.assertEqual((3,5,-1),moons[3].__repr__())
    
    def test_get_pairs(self):
        input = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""
        moons = get_moons(input)
        A,B,C,D = moons
        pairings = [[A,B],[A,C],[A,D],[B,C],[B,D],[C,D]]
        pairs = get_pairs(moons)
        self.assertEqual(pairings,pairs)
    
    def test_apply_gravity(self):
        A = Moon("<x=-1, y=0, z=2>")
        B = Moon("<x=2, y=-10, z=-7>")
        apply_gravity((A,B))
        self.assertEqual([1,-1,-1],A.velocity)
        self.assertEqual([-1,1,1],B.velocity)
    
    def test_apply_gravity_to_velocity(self):
        input = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""
        moons = get_moons(input)
        energy = tick(moons)
        
        self.assertEqual((2, -1, 1), moons[0].__repr__())
        self.assertEqual((3, -7, -4), moons[1].__repr__())
        self.assertEqual((1, -7, 5), moons[2].__repr__())
        self.assertEqual((2, 2, 0), moons[3].__repr__())

        for i in range(9):
            energy = tick(moons)
        
        self.assertEqual((2, 1, -3), moons[0].__repr__())
        self.assertEqual((1, -8, 0), moons[1].__repr__())
        self.assertEqual((3, -6, 1), moons[2].__repr__())
        self.assertEqual((2, 0, 4), moons[3].__repr__())

        self.assertEqual(36, moons[0].energy())
        self.assertEqual(179, energy)
    

    def test_apply_gravity_to_velocity_ex2(self):
        input = """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""
        moons = get_moons(input)
        for i in range(100):
            energy = tick(moons)
        self.assertEqual(1940, energy)
    
    def test_cycle_ex1(self):
        input = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""
        moons = get_moons(input)        
        tx, ty, tz = tick_cycles(moons)
        cycle = lcm(lcm(tx, ty), lcm(ty, tz))
        self.assertEqual(2772,cycle)

    def test_cycle_ex2(self):
        input = """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""
        moons = get_moons(input)
        tx, ty, tz = tick_cycles(moons)
        cycle = lcm(lcm(tx, ty), lcm(ty, tz))
        self.assertEqual(4686774924,cycle)
    
    def test_answer_matches_actual_result(self):
        input = open("input.txt").read()
        moons = get_moons(input)
        for i in range(1000):
            energy = tick(moons)
        self.assertEqual(9958, energy)
        
        moons = get_moons(input)
        tx, ty, tz = tick_cycles(moons)
        cycle = lcm(lcm(tx, ty), lcm(ty, tz))
        self.assertEqual(318382803780324, cycle)

if __name__ == '__main__':
    unittest.main()