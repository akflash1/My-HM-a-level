from datetime import datetime
import traceback

class Employee:
    SATURDAY = 5
    SUNDAY = 6
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
    ):
        super().__init__(name, salary_for_one_day, email)
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


class EmailValidator(Employee):
    def __init__(self, email: str):
        self.email = email
        self.error_logger = ErrorLogger()

    def validate_email(self, new_email):
        if new_email in self.existing_emails():
            raise EmailAlreadyExistsException
        self.email = new_email
        return '@' in self.email

    def handle_validation_error(self):
        try:
            self.validate_email()
        except EmailAlreadyExistsException as e:
            error_message = traceback.format_exc()
            print("Validation error:", error_message)
            self.error_logger.log_error(error_message)
            self.handle_validation_error()

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
developer1 = Developer("Bob", 200, tech_stack=["Python", "JavaScript"], email="bob.gmail.com")
developer2 = Developer("Antony", 150, tech_stack=["Java", "C++"], email="ant@gmail.com")


print(developer1.check_salary(10))
print(developer2.check_salary(15))
print(developer1.name)
print(developer1.tech_stack)
print(developer1.check_salary(20))
print(developer2.name)
print(developer2.tech_stack)
print(developer2.check_salary(20))
