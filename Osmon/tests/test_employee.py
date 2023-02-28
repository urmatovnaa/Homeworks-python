import unittest
from tests import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self) -> None:
        self.employee = Employee('Osmon', 'Shatmanov', 20000)

    def test_give_default_raise(self):
        self.assertEqual(self.employee.give_raise(), 25000)

    def test_give_custom_raise(self):
        self.assertEqual(self.employee.give_raise(2500), 22500)


if __name__ == '__main__':
    unittest.main()
