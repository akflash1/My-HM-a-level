students = {
    'Іван': {'Python', 'FullStack'},
    'Петро': {'FrontEnd', 'Java'},
    'Олександр': {'Python', 'Java'},
    'Анна': {'Python'},
}

print("Студенти, які навчаються у двох і більше групах:", [x for x, group in students.items() if len(group) >= 2])
print("Студенти, які не навчаються на фронтенді:", [x for x, groups in students.items() if 'FrontEnd' not in groups])
print("Студенти, які вивчають Python або Java:", [x for x, group in students.items() if 'Python' in group or 'Java' in group])
