import unittest

from password import checker, correct_length, contains_double, digits_increase

class TestPasswordChecker(unittest.TestCase):
    def test_length_too_long(self):
        input = 1134567
        self.assertFalse(correct_length(input))
    
    def test_length_too_short(self):
        input = 11345
        self.assertFalse(correct_length(input))

    def test_length_correct(self):
        input = 113456
        self.assertTrue(correct_length(input))
    
    def test_double_value_not_present(self):
        input = 123456
        self.assertFalse(contains_double(input))
    
    def test_double_value_present(self):
        input = 123356
        self.assertTrue(contains_double(input))
    
    def test_digits_not_increasing(self):
        input = 114356
        self.assertFalse(digits_increase(input))
        self.assertTrue(digits_increase(123456))
        self.assertFalse(digits_increase(1234567))
    
    def test_examples_work(self):
        input1 = 111111
        input2 = 223450
        input3 = 123789
        self.assertTrue(checker(input1))
        self.assertFalse(checker(input1, False))
        self.assertFalse(checker(input2))
        self.assertFalse(checker(input3))

if __name__ == '__main__':
    unittest.main()