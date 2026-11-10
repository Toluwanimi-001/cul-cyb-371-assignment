import csv
import random

matric_number = "24/15284"
student_name = "Akinyemi Toluwanimi Oluwafumbi"
course_code = "CUL CYB 371"

departments = ['Computer Science', 'Mathematics', 'Physics', 'Biology', 'Economics']
levels = ['100 Level', '200 Level', '300 Level', '400 Level']

rows = []
for i in range(1, 51):
    s_id = "STU" + str(i).zfill(3)
    dept = random.choice(departments)
    lvl = random.choice(levels)
    attendance = round(random.uniform(50.0, 100.0), 2)
    score = round(random.uniform(35.0, 98.0), 2)
    rows.append([s_id, dept, lvl, attendance, score])

with open("student_dataset.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Student ID", "Department", "Level", "Attendance Percentage", "Average Examination Score"])
    writer.writerows(rows)

info_text = f"Course: {course_code}\nName: {student_name}\nMatric Number: {matric_number}\n"
with open("student_info.txt", mode="w", encoding="utf-8") as file:
    file.write(info_text)
