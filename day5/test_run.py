import unittest
  
class TestRun(unittest.TestCase):
    def test_foo(self):
        input = True
        self.assertTrue(input)

if __name__ == '__main__':
    unittest.main()