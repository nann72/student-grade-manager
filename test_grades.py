import unittest
from grades import add_student, calculate_average, get_top_student

class TestGrades(unittest.TestCase):
    def setUp(self):
        self.data = {"Анна": 90, "Богдан": 80}

    def test_add_student_success(self):
        res = add_student(self.data, "Олег", 85)
        self.assertEqual(res["Олег"], 85)

    def test_add_student_invalid(self):
        with self.assertRaises(ValueError):
            add_student(self.data, "Марія", 150)

    def test_calculate_average(self):
        self.assertEqual(calculate_average(self.data), 85.0)

    def test_get_top_student(self):
        self.assertEqual(get_top_student(self.data), "Анна")

if __name__ == "__main__":
    unittest.main()