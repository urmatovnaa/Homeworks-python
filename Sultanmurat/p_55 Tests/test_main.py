import unittest

from main import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Alex', 'Macbookoff', 10000)
    
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 15000)

    def test_give_custom_raise(self):
        self.employee.give_raise(1000)
        self.assertEqual(self.employee.salary, 11000)


if __name__ == '__main__':
    unittest.main()