import unittest
from zork_droid import ZorkDroid
from keyboard import Keyboard

class ZorkDroidTest(unittest.TestCase):
    def test_zorkdroid_program_move(self):
        kb = Keyboard()
        droid = ZorkDroid("input.txt", kb)
        finished, output = droid.move()
        expected = \
"""== Hull Breach ==
You got in through a hole in the floor here. To keep your ship from also freezing, the hole has been sealed.

Doors here lead:
- north
- west"""
        self.assertEqual("".join(output), expected)
        self.assertFalse(finished)

    def test_zorkdroid_program_parse(self):
        kb = Keyboard()
        droid = ZorkDroid("input.txt", kb)
        finished, output = droid.move()
        room, desc, doors, items = droid.parse(output)

        self.assertEqual(room,"Hull Breach")
        self.assertEqual(desc,"You got in through a hole in the floor here. To keep your ship from also freezing, the hole has been sealed.")
        self.assertEqual(doors,["north", "west"])
        self.assertEqual(items,[])
        self.assertFalse(finished)

    def test_zorkdroid_program_parse_2(self):
        kb = Keyboard()
        input = ["north\n"]
        for command in input:
                kb.append(command)
        droid = ZorkDroid("input.txt", kb)
        finished, output = droid.move()
        finished, output = droid.move()
        room, desc, doors, items = droid.parse(output)

        self.assertEqual(room,"Observatory")
        self.assertEqual(desc,"There are a few telescopes; they're all bolted down, though.")
        self.assertEqual(doors,["north", "east", "south"])
        self.assertEqual(items,["dark matter"])
        self.assertFalse(finished)

if __name__ == '__main__':
    unittest.main()


