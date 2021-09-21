# 02. Average Student Grades
n = int(input())
students_book = {}

for _ in range(n):
    students = input().split()
    student_name = students[0]
    student_grade = float(students[1])
    if student_name not in students_book:
        students_book[student_name] = []
    students_book[student_name].append(student_grade)

for (student_key, grades_values) in students_book.items():
    grades_as_str = ' '.join(map(lambda grade: f'{grade:.2f}', grades_values))
    average = sum(grades_values) / len(grades_values)
    print(f"{student_key} -> {grades_as_str} (avg: {average:.2f})")