import unittest
from tests import Employee


class Test_employee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("adil", "t", 50000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.year_salary, 55000)

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.year_salary, 60000)


if __name__ == '__main__':
    unittest.main()
