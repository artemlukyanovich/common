import unittest
from python_functions import fun1, fun2, fun3, fun4, fun5, fun6

class Tests(unittest.TestCase):
    def test_fun1(self):
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.assertEqual(fun1(a, b), [1, 2, 3, 5, 8, 13])

    def test_fun2(self):
        a = "I am a good developer. I am also a writer"
        self.assertEqual(fun2(a), 5)

    def test_fun3(self):
        self.assertEqual(fun3(9), True)

    def test_fun4(self):
        self.assertEqual(fun4(48), 3)
        self.assertEqual(fun4(999), 9)

    def test_fun5(self):
        self.assertEqual(fun5([0,2,3,4,6,7,10]), [2, 3, 4, 6, 7, 10, 0])

    def test_fun6(self):
        self.assertEqual(fun6([5, 7, 9, 11]), True)

