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

    def test_answer_matches_actual_solution(self):
        pt1 = 0
        pt2 = 0
        lower = 264793
        upper = 803935
        for input in range(lower, upper):
            if checker(input, True): pt1+=1
            if checker(input, False): pt2+=1
        self.assertEqual(966, pt1)
        self.assertEqual(628, pt2)

if __name__ == '__main__':
    unittest.main()