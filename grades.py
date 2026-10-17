def add_student(grades_dict, name, grade):
    if not (0 <= grade <= 100):
        raise ValueError("Оцінка має бути від 0 до 100")
    grades_dict[name] = grade
    return grades_dict
