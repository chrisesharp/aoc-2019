import unittest

from fft import apply_fft, calc_pattern

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

if __name__ == '__main__':
    unittest.main()