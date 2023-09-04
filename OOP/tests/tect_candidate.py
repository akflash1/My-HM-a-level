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

    def test_init(self):
        name = 'name_2'
        email = 'mail@gmail.com'
        tech_stack = 'Java'
        main_skill = 'Development'
        main_skill_grade = 'Jun'

        candidate_2 = Candidate(
            first_name=name,
            last_name=self.last_name,
            email=email,
            tech_stack=tech_stack,
            main_skill=main_skill,
            main_skill_grade=main_skill_grade
        )

        self.assertEqual(name, candidate_2.first_name)
        self.assertEqual(self.last_name, candidate_2.last_name)
        self.assertEqual(email, candidate_2.email)
        self.assertEqual(tech_stack, candidate_2.tech_stack)
        self.assertEqual(main_skill, candidate_2.main_skill)
        self.assertEqual(main_skill_grade, candidate_2.main_skill_grade)

    def test_full_name(self):
        self.assertEqual(self.first_name + ' ' + self.last_name, self.candidate.full_name)

    @patch('requests.get')
    def test_generate_candidates(self, mock_get):
        mock_get.return_value.text = 'John,Doe,johndoe@gmail.com,Python|Java,Junior\n' \
                                     'Alice,Smith,alice@gmail.com,JavaScript,Senior'

        url = 'https://example.com/candidates.csv'
        email_validator = EmailValidator()
        email_validator.test_emails = ['alice@gmail.com']

        candidates = Candidate.generate_candidates(url)

if __name__ == '__main__':
    unittest.main()
