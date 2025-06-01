# Task 1: Create a Dictionary of Student Marks
student_name = {'Alice': 85, 'Charlie': 75,'Michael': 90,'Bob': 55}
name = (input('Enter student name: '))
if name in student_name:
    print(f"{name}'s marks: {student_name[name]}")
else:
    print('Student not found.')


