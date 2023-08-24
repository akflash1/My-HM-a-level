import requests
from datetime import datetime
import traceback

SATURDAY = 5
SUNDAY = 6

class Employee:

    WEEKEND = (SATURDAY, SUNDAY)

    def __init__(
            self,
            name: str,
            salary_for_one_day: int,
            email: str,
    ):
        self.name = name
        self.salary_for_one_day = salary_for_one_day
        self.email = email

    def work(self):
        return 'I come to the office.'

    def __str__(self):
        return f'Position: {self.name}'

    def __eq__(self, other):
        return self.salary_for_one_day == other.salary_for_one_day

    def __lt__(self, other):
        return self.salary_for_one_day < other.salary_for_one_day

    def __le__(self, other):
        return self.salary_for_one_day <= other.salary_for_one_day

    def __gt__(self, other):
        return self.salary_for_one_day > other.salary_for_one_day

    def __ge__(self, other):
        return self.salary_for_one_day >= other.salary_for_one_day

    def __ne__(self, other):
        return self.salary_for_one_day != other.salary_for_one_day

    def check_salary(self, days):
        weekday = datetime.now().weekday()
        if weekday not in self.WEEKEND:
            return f'Salary for the transferred number of days: {self.salary_for_one_day * days}'
        else:
            return 'No salary today.'


class Developer(Employee):
    def __init__(
            self,
            name: str,
            salary_for_one_day: int,
            email: str,
            tech_stack=None,
            *args,
            **kwargs,
    ):
        super().__init__(name, salary_for_one_day, email, *args, **kwargs)
        self.tech_stack = tech_stack if tech_stack is not None else []

    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)

    def __add__(self, other):
        new_name = f'{self.name} {other.name}'
        new_tech_stack = list(set(self.tech_stack + other.tech_stack))
        new_salary = max(self.salary_for_one_day, other.salary_for_one_day)
        return Developer(new_name, new_salary, new_tech_stack, self.email)

    def work(self):
        return f'{super().work()} and start to coding.'


class Recruiter(Employee):
    def work(self):
        return f'{super().work()} and start to hiring.'


class Candidate(Employee):
    def __init__(self,
                first_name: str,
                last_name: str,
                email,
                tech_stack: str,
                main_skill: str,
                main_skill_grade: str,
    ):
        self.first_name = first_name
        self. last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def generate_candidates(cls, url):
        response = requests.get(url)
        candidates = []
        lines = response.text.split('\n')
        header = lines[0]
        for line in lines[1:]:
            parts = line.strip().split(',')
            if len(parts) == 5:
                first_name, last_name, email, tech_stack, main_skill_grade = parts
                main_skill = tech_stack.split('|')[0]
                candidate = cls(first_name, last_name, email, tech_stack, main_skill, main_skill_grade)
                candidates.append(candidate)
        return candidates


class EmailValidator:
    def __init__(self, email: str):
        self.email = email
        self.error_logger = ErrorLogger()

    @classmethod
    def validate_email(cls, new_email):
        if new_email in cls.existing_emails():
            raise EmailAlreadyExistsException
        return '@' in new_email

    def handle_validation_error(self, attempts = 0):
        if attempts > 5:
            print("Max attempts reached.")
            return
        try:
            self.validate_email()
        except EmailAlreadyExistsException as e:
            error_message = traceback.format_exc()
            print("Validation error:", error_message)
            self.error_logger.log_error(error_message)
            self.handle_validation_error(attempts + 1)

    def existing_emails(self):
        with open('emails.csv', 'r') as file:
            return file.read().splitlines()


class ErrorLogger:
    def log_error(self, error_message):
            print("Logging error:", error_message)
            with open('logs.txt', 'a') as file:
                file.write(f'{datetime.now()} | {error_message}\n')


class EmailWriter(Employee):
    def save_email(self, email: str):
        with open('emails.csv', 'a') as file:
            file.write(f'{self.email}\n')


employee1 = Employee("John", 100, email="john@gmail.com")
recruiter1 = Recruiter("Alice", 150, email="alice@gmail.com")
developer1 = Developer("Bob", 200, tech_stack=["Python", "JavaScript"], email="bobgmail.com")
developer2 = Developer("Antony", 150, tech_stack=["Java", "C++"], email="ant@gmail.com")

candidate_objects = Candidate.generate_candidates('https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv')

for candidate in candidate_objects:
    print(f"Full Name: {candidate.full_name}")
    print(f"Email: {candidate.email}")
    print(f"Tech Stack: {candidate.tech_stack}")
    print(f"Main Skill: {candidate.main_skill}")
    print(f"Main Skill Grade: {candidate.main_skill_grade}")
    print("---")
