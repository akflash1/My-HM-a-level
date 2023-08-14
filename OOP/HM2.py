class Employee:
    def __init__(self, name, salary_for_one_day,):
        self.name = name
        self.salary_for_one_day = salary_for_one_day

    def work(self):
        return f'I come to the office.'

    def __str__(self):
        return f'Position: {self.name}'

    def __eq__(self, other):
        return self.salary_for_one_day == other.salary_for_one_day


class Recruiter(Employee):
    def work(self):
        return f'I come to the office and start to hiring.'


class Developer(Employee):
    def work(self):
        return f'I come to the office and start to coding.'

employee1 = Employee("John", 100)
recruiter1 = Recruiter("Alice", 150)
developer1 = Developer("Bob", 200)

