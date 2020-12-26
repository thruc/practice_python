import unittest
from cluc import Culc



class CalcTest(unittest.TestCase):
    def test_add_num_and_double(self):
        cal = Culc()

        self.assertAlmostEqual(cal.add_and_doubel(1, 1), 4)

if __name__ == "__main__":
    unittest.main()
    