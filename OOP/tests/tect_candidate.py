import unittest
from HM2_2 import Candidate


class CandidateTest(unittest.TestCase):
    def setUp(self):
        self.first_name = 'Jake'
        self.last_name = 'Doe'
        self.email = 'email@gmail.com'
        self.tech_stack = 'Python'
        self.main_skill = 'Coding'
        self.main_skill_grade = 'Midl'
        self.candidate = Candidate(
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            tech_stack=self.tech_stack,
            main_skill=self.main_skill,
            main_skill_grade=self.main_skill_grade
        )

    def test_full_name(self):
        self.assertEqual(self.first_name + ' ' + self.last_name, self.candidate.full_name)

    @patch('requests.get')
    def test_generate_candidates(self, mock_get):
        mock_get.return_value.text = 'John,Doe,johndoe@gmail.com,Python|Java,Junior\n' \
                                     'Alice,Smith,alice@gmail.com,JavaScript,Senior'

        url = 'https://example.com/candidates.csv'

        candidates = Candidate.generate_candidates(url)

        self.assertEqual(len(candidates), 2)
        self.assertEqual(candidates[0].first_name, 'John')
        self.assertEqual(candidates[0].last_name, 'Doe')
        self.assertEqual(candidates[0].email, 'johndoe@gmail.com')
        self.assertEqual(candidates[0].tech_stack, 'Python|Java')
        self.assertEqual(candidates[0].main_skill, 'Junior')

        self.assertEqual(candidates[1].first_name, 'Alice')
        self.assertEqual(candidates[1].last_name, 'Smith')
        self.assertEqual(candidates[1].email, 'alice@gmail.com')
        self.assertEqual(candidates[1].tech_stack, 'JavaScript')
        self.assertEqual(candidates[1].main_skill, 'Senior')

if __name__ == '__main__':
    unittest.main()
