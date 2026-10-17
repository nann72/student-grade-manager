def add_student(grades_dict, name, grade):
    if not (0 <= grade <= 100):
        raise ValueError("Оцінка має бути від 0 до 100")
    grades_dict[name] = grade
    return grades_dict

git add grades.py
git commit -m "Коміт 2: Створено базовий модуль з функцією додавання студентів"
