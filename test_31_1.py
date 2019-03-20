import unittest
from test_31 import Employee


class NamesTestCase(unittest.TestCase):
    """测试city_function.py"""
    def setUp(self):
        self.employee = Employee('ergou', 'yang','5000')
        self.Raise_setup = [5000,6000]

    def test_give_default_raise(self):
        # employee1 = Employee('ergou', 'yang','5000')
        self.assertEqual(self.employee.give_raise(), 10000)

    def test_give_custom_raise(self):
        # employee2 = Employee('ergou', 'yang','5000')
        self.employee.Raise = self.Raise_setup[1]
        self.assertEqual(self.employee.give_raise(), 11000)


if __name__=="__main__":
    unittest.main()
