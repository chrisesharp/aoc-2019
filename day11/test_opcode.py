import unittest

from opcodes import Processor

class OpCodeTest(unittest.TestCase):    
    def test_ex1_position(self):
        inst = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        for i in [0,1]:
            processor = Processor(inst)
            output = processor.run([i])
            self.assertEqual([i],output)
    
    def test_ex2_8_gives_1000(self):
        processor = Processor([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])
        output = processor.run([8])
        self.assertEqual([1000], output)

    def test_ex2_9_gives_1001(self):
        processor = Processor([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])
        output = processor.run([9])
        self.assertEqual([1001], output)
    
    def test_ex1_relative(self):
        prog = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
        processor = Processor(prog, 120, True)
        output = processor.run([])
        self.assertEqual(prog, output)
    
    def test_ex2_relative(self):
        prog = [1102,34915192,34915192,7,4,7,99,0]
        processor = Processor(prog, 120, True)
        output = processor.run([])
        answer = 34915192*34915192
        self.assertEqual(answer, output[0])
    
    def test_ex3_relative(self):
        prog = [104,1125899906842624,99]
        processor = Processor(prog, 120, True)
        output = processor.run([])
        answer = 1125899906842624
        self.assertEqual(answer, output[0])

if __name__ == '__main__':
    unittest.main()