import unittest

from opcodes import execute, fetch, run, program

class OpCodeTest(unittest.TestCase):
    def test_opcode_1_123(self):
        instruction = [1, 1, 2, 3]
        instruction = execute(instruction, instruction)
        self.assertEqual(instruction[3], 3)

    def test_opcode_2_123(self):
        instruction = [2, 1, 0, 1]
        instruction = execute(instruction, instruction)
        self.assertEqual(instruction[1], 2)
    
    def test_fetch(self):
        instructions = [1,0,0,0,99]
        instr, ip = fetch(instructions)
        self.assertEqual([1,0,0,0], instr)
        self.assertEqual(4, ip)
    
    def test_ex0(self):
        instructions = run([1,9,10,3,2,3,11,0,99,30,40,50])
        self.assertEqual([3500,9,10,70,2,3,11,0,99,30,40,50], instructions)
    
    def test_ex1(self):
        instructions = run([1,0,0,0,99])
        self.assertEqual([2,0,0,0,99], instructions)
    
    def test_ex2(self):
        instructions = run([2,3,0,3,99])
        self.assertEqual([2,3,0,6,99], instructions)
    
    def test_ex3(self):
        instructions = run([2,4,4,5,99,0])
        self.assertEqual([2,4,4,5,99,9801], instructions)
    
    def test_ex4(self):
        instructions = run([1,1,1,4,99,5,6,0,99])
        self.assertEqual([30,1,1,4,2,5,6,0,99], instructions)
    
    def test_program(self):
        instructions = [1,1,1,4,99,5,6,0,99,0,0,0,0]
        prog = program(instructions, 12, 2)
        self.assertEqual([1,12,2,4,99,5,6,0,99,0,0,0,0], prog)

if __name__ == '__main__':
    unittest.main()