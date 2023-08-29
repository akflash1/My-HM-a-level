import unittest
from datetime import datetime
from unittest.mock import patch
from HM2_2 import Employee

class TestEmployee(unittest.TestCase):

    @patch('datetime.datetime')
    def test_check_salary_weekday(self, mock_datetime):
        employee = Employee("John", 500, email="john@gmail.com")
        datetime_now = datetime(2023, 8, 28)
        mock_datetime.now.return_value = datetime_now
        self.assertEqual(employee.check_salary(5), "Salary for the transferred number of days: 2500")

    @patch('datetime.datetime')
    def test_check_salary_weekend(self, mock_datetime):
        employee = Employee("John", 0, email="john@gmail.com")
        datetime_now = datetime(2023, 8, 26)
        mock_datetime.now.return_value = datetime_now
        self.assertEqual(employee.check_salary(5), "Salary for the transferred number of days: 0")

    def test_comparison(self):
        employee1 = Employee("John", 100, email="john@gmail.com")
        employee2 = Employee("Alice", 150, email="alice@gmail.com")

        self.assertTrue(employee1 < employee2)
        self.assertFalse(employee1 > employee2)
        self.assertTrue(employee1 <= employee2)
        self.assertFalse(employee1 >= employee2)
        self.assertFalse(employee1 == employee2)
        self.assertTrue(employee1 != employee2)

if __name__ == '__main__':
    unittest.main()
