def add_student(grades_dict, name, grade):
    if not (0 <= grade <= 100):
        raise ValueError("Оцінка має бути від 0 до 100")
    grades_dict[name] = grade
    return grades_dict

def calculate_average(grades_dict):
    if not grades_dict:
        return 0.0
    return sum(grades_dict.values()) / len(grades_dict)

def get_top_student(grades_dict):
    if not grades_dict:
        return None
    return max(grades_dict, key=grades_dict.get)