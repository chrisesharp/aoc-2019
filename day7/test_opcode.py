import unittest

from opcodes import Processor

class OpCodeTest(unittest.TestCase):    
    def test_ex1_position(self):
        inst = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        for i in [0,1]:
            processor = Processor(inst)
            output = processor.run([i])
            self.assertEqual(i,output)
    
    def test_ex1_immediate(self):
        inst = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
        for i in [0,1]:
            processor = Processor(inst)
            output = processor.run([i])
            self.assertEqual(i,output)

    def test_ex2_1_gives_999(self):
        processor = Processor([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])
        output = processor.run([1])
        self.assertEqual(999, output)
    
    def test_ex2_8_gives_1000(self):
        processor = Processor([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])
        output = processor.run([8])
        self.assertEqual(1000, output)

    def test_ex2_9_gives_1001(self):
        processor = Processor([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])
        output = processor.run([9])
        self.assertEqual(1001, output)


if __name__ == '__main__':
    unittest.main()