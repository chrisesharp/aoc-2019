import unittest

from reactor import get_reactions, ore_required

class ReactorTest(unittest.TestCase):    
    def test_parse_input(self):
        input = """10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL"""
        reactions = get_reactions(input)
        print(reactions)
        self.assertEqual(31, ore_required(reactions))

if __name__ == '__main__':
    unittest.main()