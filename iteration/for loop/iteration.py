
# Instruction
'''''
A List of scores of students are given, 
implement a program that calculates the highest score from the given list.
'''''

student_scores = [20, 60, 50, 65, 75, 55]
highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f'The highest score is {highest_score}')