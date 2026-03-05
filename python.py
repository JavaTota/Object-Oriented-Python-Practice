import re

class Student:
    def __init__(self, name, email, grades):
        self.name = name
        self.email = email
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0.0

    def display_info(self):
        print(f"Name: {self.name}, Email: {self.email}")

    def grades_tuple(self):
        return tuple(self.grades)


# Create students
student1 = Student("Alice", "alice@gmail.com", [85, 90, 78])
student2 = Student("Marco", "marco@gmail.com", [92, 88, 95])
student3 = Student("Fra", "fra@gmail.com", [85, 80, 78])


# Add grades
student1.add_grade(92)
student1.add_grade(88)

student2.add_grade(85)
student2.add_grade(90)

student3.add_grade(88)
student3.add_grade(82)


# Print info + average
for student in [student1, student2, student3]:
    student.display_info()
    print(f"Average Grade: {student.calculate_average():.2f}")


# Dictionary of students
student_dict = {
    student1.email: student1,
    student2.email: student2,
    student3.email: student3
}


# Safe lookup
def get_student_by_email(email):
    student = student_dict.get(email)
    if student:
        return student
    print(f"No student found with email: {email}")
    return None


# Unique grades
unique_grades = set()
for student in student_dict.values():
    unique_grades.update(student.grades)

print("Unique Grades:", unique_grades)


# Tuple immutability demo
try:
    student1.grades_tuple()[0] = 100
except TypeError as e:
    print("Cannot modify grades tuple:", e)


# Remove last grade
for student in student_dict.values():
    if student.grades:
        student.grades.pop()


# First and last grade
for student in student_dict.values():
    if student.grades:
        print(f"{student.name}'s first grade: {student.grades[0]}, last grade: {student.grades[-1]}")
    else:
        print(f"{student.name} has no grades.")


# Number of grades
for student in student_dict.values():
    print(f"{student.name} has {len(student.grades)} grades.")


# Email validation
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

for student in student_dict.values():
    if re.match(email_pattern, student.email):
        print(f"{student.name}'s email is valid.")
    else:
        print(f"{student.name}'s email is invalid.")


# Count grades above 90
count = 0
for student in student_dict.values():
    for grade in student.grades:
        if grade > 90:
            count += 1

print("Number of grades above 90:", count)