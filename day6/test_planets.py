import unittest

from planets import StarMap

class TestRun(unittest.TestCase):
    def test_orbits_example(self):
        input = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
"""
        mapper = StarMap(input.split())
        self.assertEqual(11,len(mapper.planets)-1)
        self.assertEqual(1,mapper.planets[1].total_orbits())
        self.assertEqual(2,mapper.planets[2].total_orbits())
    
    def test_path_example(self):
        input = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
"""
        mapper = StarMap(input.split())
        path = mapper.find_path("L", "D")
        self.assertEqual(4,len(path)-1)

    def test_answer_matches_actual_solution(self):
        file = open("input.txt","r").readlines()
        starmap = StarMap(file)
        count = 0
        for planet in starmap.planets:
            count += planet.total_orbits()
        self.assertEqual(249308, count)

        path = starmap.find_path("YOU", "SAN")
        self.assertEqual(349, len(path) - 1)

if __name__ == '__main__':
    unittest.main()