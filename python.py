# Define a Student class with attributes for name, email, and grades (a list of numbers).
class Student:
    def __init__(self, name, email, grades):
        self.name = name
        self.email = email
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)
    
    def calculate_average(self):
        if self.grades:
            average = sum(self.grades) / len(self.grades)
            return average
        else:
            return 0.0
    def display_info(self):
        print(f"Name: {self.name}, Email: {self.email}")

#Create 3 student objects with different names, emails, and initial grades.
student1 = Student("Alice", "alice@gmail.com", [85, 90, 78])
student2 = Student("Marco", "marco@gmail.com", [92, 88, 95])
student3 = Student("Fra", "fra@gmail.com", [85, 80, 78])

#Add 2 new grades to each student using the add_grade method.
student1.add_grade(92)
student1.add_grade(88)
student2.add_grade(85)
student2.add_grade(90)
student3.add_grade(88)
student3.add_grade(82)

#Print the information and average grade for each student using display_info.
student1.display_info()
print(f"Average Grade: {student1.calculate_average():.2f}")
student2.display_info()
print(f"Average Grade: {student2.calculate_average():.2f}")
student3.display_info()
print(f"Average Grade: {student3.calculate_average():.2f}")

#Create a dictionary called student_dict that maps each student’s email to their corresponding Student object.
student_dict = {
    student1.email: student1,
    student2.email: student2,
    student3.email: student3
}

#Write a function get_student_by_email(email) that retrieves a student object from the dictionary safely using .get().
def get_student_by_email(email):
    student = student_dict.get(email)
    if student:
        return student
    else:
        print(f"No student found with email: {email}")
        return None
    
#Create a set of all unique grades across all students and print it.
unique_grades = set()
for student in student_dict.values():
    unique_grades.update(student.grades)
print(f"Unique Grades: {unique_grades}")

#Add a method to the Student class called grades_tuple(self) that returns the grades as a tuple.
class Student:
    def __init__(self, name, email, grades):
        self.name = name
        self.email = email
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)
    
    def calculate_average(self):
        if self.grades:
            average = sum(self.grades) / len(self.grades)
            return average
        else:
            return 0.0
    
    def display_info(self):
        print(f"Name: {self.name}, Email: {self.email}")
    
    def grades_tuple(self):
        return tuple(self.grades)
    
#Demonstrate that tuples are immutable by trying to change a value (catch the exception with try/except and print a message).
try:
    student1.grades_tuple()[0] = 100
except TypeError as e:
    print(f"Cannot modify grades tuple: {e}")

#Remove the last grade from each student’s grades list using .pop().
student1.grades.pop()
student2.grades.pop()
student3.grades.pop()

#Access and print the first and last grade for each student.
for student in student_dict.values():
    if student.grades:
        print(f"{student.name}'s first grade: {student.grades[0]}, last grade: {student.grades[-1]}")
    else:
        print(f"{student.name} has no grades.")

#Print the number of grades each student has using len().
for student in student_dict.values():
    print(f"{student.name} has {len(student.grades)} grades.")

#Use regular expressions to validate that each student’s email follows the format: name@domain.com.
import re
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
for student in student_dict.values():
    if re.match(email_pattern, student.email):
        print(f"{student.name}'s email is valid.")
    else:
        print(f"{student.name}'s email is invalid.")

#Count how many grades are above 90 across all students.
count = 0
for student in student_dict.values():
    for grade in student.grades:
        if grade > 90:
            count += 1
print(f"Number of grades above 90: {count}")