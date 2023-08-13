def average_grade(grades):
    return sum(grades) / len(grades)
    students_grades = {
        'Іван': [80, 90, 70],
        'Петро': [75, 85, 95],
        'Олександр': [60, 70, 65],
        'Анна': [90, 80, 85],
}

best_student = max(students_grades, key=lambda student: average_grade(students_grades[student]))
worst_student = min(students_grades, key=lambda student: average_grade(students_grades[student]))

print(f'Найуспішніший студент: {best_student}, середній бал: {average_grade(students_grades[best_student])}')
print(f'Найслабший студент: {worst_student}, середній бал: {average_grade(students_grades[worst_student])}')
