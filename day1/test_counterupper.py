import unittest

from counter_upper import fuel_calc, fuel_calc2

class CounterUpperTest(unittest.TestCase):
    def test_counterupper_12(self):
        mass = 12
        expected_fuel = 2
        calc = fuel_calc(mass)
        self.assertEqual(expected_fuel, calc)
    
    def test_counterupper_14(self):
        mass = 14
        expected_fuel = 2
        calc = fuel_calc(mass)
        self.assertEqual(expected_fuel, calc)
    
    def test_counterupper_1969(self):
        mass = 1969
        expected_fuel = 654
        calc = fuel_calc(mass)
        self.assertEqual(expected_fuel, calc)

    def test_counterupper_100756(self):
        mass = 100756
        expected_fuel = 33583
        calc = fuel_calc(mass)
        self.assertEqual(expected_fuel, calc)
    
    def test_counterupper_2_14(self):
        mass = 14
        expected_total_fuel = 2
        calc = fuel_calc2(mass)
        self.assertEqual(expected_total_fuel, calc)
    
    def test_counterupper_2_1969(self):
        mass = 1969
        expected_total_fuel = 966
        calc = fuel_calc2(mass)
        self.assertEqual(expected_total_fuel, calc)
    
    def test_counterupper_2_100756(self):
        mass = 100756
        expected_total_fuel = 50346
        calc = fuel_calc2(mass)
        self.assertEqual(expected_total_fuel, calc)
    
    def test_answer_matches_actual_solution(self):
        total = 0
        file = open("input.txt", "r")
        for line in file:
            total += fuel_calc2(int(line))
        self.assertEqual(5055835, total)

if __name__ == '__main__':
    unittest.main()