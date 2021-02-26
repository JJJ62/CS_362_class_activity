import unittest
import fibonacci

class TestFibonacci(unittest.TestCase):
    def TestFirst(self):
        result = fibonacci.get_fibonacci(0)
        self.assertEqual(result, 0)

    def TestSecond(self):
        result = fibonacci.get_fibonacci(1)
        self.assertEqual(result, 1)

    def TestThird(self):
        result = fibonacci.get_fibonacci(2)
        self.assertEqual(result, 1)

    def TestThird(self):
        result = fibonacci.get_fibonacci(3)
        self.assertEqual(result, 2)

    def Testfourth(self):
        result = fibonacci.get_fibonacci(4)
        self.assertEqual(result, 3)

    def Testfifth(self):
        result = fibonacci.get_fibonacci(5)
        self.assertEqual(result, 5)
