'''
Implement a function which takes a dictionary as a parameter in which student scores are stored and
converts their scores to grades and return it as new dictionary.

This is the scoring criteria:

Scores 85 - 100: Grade = "Outstanding"
Scores 65 - 84: Grade = "Good"
Scores 50 - 64: Grade = "Acceptable"
Scores 50 lower: Grade = "Fail"
'''
student_scores = {
  "John": 90,
  "Edy": 68,
  "Marry": 88,
  "Ewan": 79,
  "Park": 62,
}

def convert_grade(p_dict):
    student_grades = {}
    for key in p_dict:
        score = p_dict[key]
        if score >= 85:
            student_grades[key] = "Outstanding"
        elif score >= 65:
            student_grades[key] = "Good"
        elif score >= 50:
            student_grades[key] = "Acceptable"
        else:
           student_grades[key] = "Fail"
    return student_grades


print(convert_grade(student_scores))