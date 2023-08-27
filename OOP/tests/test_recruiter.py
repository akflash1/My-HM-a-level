import unittest
from HM2_2 import Recruiter

class RecruiterTest(unittest.TestCase):
    def test_work(self):
        recruiter = Recruiter("John", 500, "john@example.com")
        result = recruiter.work()
        expected_result = 'I come to the office. and start to hiring.'
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
