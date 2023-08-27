import unittest
from HM2_2 import Developer

class DeveloperTest(unittest.TestCase):
    def setUp(self):
        self.developer1 = Developer(name='John', salary_for_one_day=200, email='john@example.com', tech_stack=['Python', 'JavaScript'])
        self.developer2 = Developer(name='Alice', salary_for_one_day=180, email='alice@example.com', tech_stack=['Java', 'C++'])

    def test_init(self):
        self.assertEqual(self.developer1.name, 'John')
        self.assertEqual(self.developer1.salary_for_one_day, 200)
        self.assertEqual(self.developer1.email, 'john@example.com')
        self.assertEqual(self.developer1.tech_stack, ['Python', 'JavaScript'])

    def test_eq(self):
        self.assertTrue(self.developer1 == self.developer1)
        self.assertTrue(self.developer1 != self.developer2)

    def test_work(self):
        expected_output = "I come to the office. and start to coding."
        self.assertEqual(self.developer1.work(), expected_output)

if __name__ == '__main__':
    unittest.main()
