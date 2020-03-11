import unittest

from fft import apply_fft, calc_pattern, part1, part2

class FFTTest(unittest.TestCase):
    def test_fft_ex1(self):
        input = "12345678"
        output = apply_fft(input)
        self.assertEqual("48226158", output)
    
    def test_fft_ex2(self):
        input = "12345678"
        output = apply_fft(apply_fft(apply_fft(input)))
        self.assertEqual("03415518", output)
    
    def test_fft_ex3(self):
        input = "12345678"
        output = apply_fft(apply_fft(apply_fft(apply_fft(input))))
        self.assertEqual("01029498", output)

    def test_fft_ex4(self):
        input = "80871224585914546619083218645595"

        length = len(str(input))
        for i in range(100):
            output = apply_fft(input, length)
            input = output
        output = str(output)[:8]
        self.assertEqual("24176176", output)
    
    def test_fft_ex5(self):
        input = "19617804207202209144916044189917"

        length = len(str(input))
        for i in range(100):
            output = apply_fft(input,length)
            input = output
        output = str(output)[:8]
        self.assertEqual("73745418", output)
    
    def test_fft_ex6(self):
        input = "69317163492948606335995924319873"

        length = len(str(input))
        for i in range(100):
            output = apply_fft(input, length)
            input = output
        output = str(output)[:8]
        self.assertEqual("52432133", output)
    
    def test_part1_ex1(self):
        input = "69317163492948606335995924319873"
        output = part1(input)
        self.assertEqual(52432133, output)
    
    def test_part2_ex1(self):
        input = "03036732577212944063491565474664"
        output = part2(input)
        self.assertEqual(84462026, output)
    
    def test_part2_ex2(self):
        input = "02935109699940807407585447034323"
        output = part2(input)
        self.assertEqual(78725270, output)
    
    def test_part2_ex3(self):
        input = "03081770884921959731165446850517"
        output = part2(input)
        self.assertEqual(53553731, output)
    
    def test_answer_matches_actual_solution(self):
        input = open("input.txt").readline().strip()
        self.assertEqual(82525123, part1(input))
        self.assertEqual(49476260, part2(input))

if __name__ == '__main__':
    unittest.main()