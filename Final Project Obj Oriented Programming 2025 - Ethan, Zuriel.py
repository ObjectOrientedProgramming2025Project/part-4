#Zuriel Tolibas, Ethan Baird March 28, 2025

import csv

#Class representing the student
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = {}  #Dictionary to store course names

    #Enrolling the student in course if not already enrolled
    def add_course(self, course):
        if course.course_code not in self.courses:
            self.courses[course.course_name] = []
        else:
            print("Student already enrolled in this course.")

    #Adding grade for specific course if student is enrolled
    def add_grade(self, course_name, grade):
        if course_name in self.courses:
            self.courses[course_name].append(grade)
        else:
            print("Student is not enrolled in this course.") 

    #To calculate and return the studnet's average grade for all of their enrolled courses
    def calculate_average(self):
        total, count = 0, 0
        for grades in self.courses.values():
            total += sum(grades)
            count += len(grades)
        return total / count if count else 0

    #Converting the number grade to a letter grade
    def get_letter_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

#Class representing a course
class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name
        
#Class representing the student grading sustem
class StudentGradingSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.load_data()

    #Prompts for student to enter their details and adding it to the system
    def add_student(self):
        #Prompt for user to input their ID
        student_id = input("Enter student ID: ")
        if student_id in self.students:
            print("Student ID already exists.")
            return
        #Prompt for user to input name
        name = input("Enter student name: ")
        self.students[student_id] = Student(student_id, name)
        self.save_data()

    def add_course(self):
        #Prompt for user to input course code
        course_code = input("Enter course code: ")
        if course_code in self.courses:
            print("Course already exists.")
            return
        #Prompt for user to input course name
        course_name = input("Enter course name: ")
        self.courses[course_code] = Course(course_code, course_name)
        self.save_data()

    #Enrolling student in course if their name is in the systme
    def enroll_student(self):
        student_id = input("Enter student ID: ")
        if student_id not in self.students:
            print("Student not found.")
            return
        course_code = input("Enter course code: ")
        if course_code not in self.courses:
            print("Course not found.")
            return
        self.students[student_id].add_course(self.courses[course_code])
        self.save_data()

    def add_grade(self):
        student_id = input("Enter student ID: ")
        if student_id not in self.students:
            print("Student not found.")
            return
        course_code = input("Enter course code: ")
        if course_code not in self.courses:
            print("Course not found.")
            return
        course_name = self.courses[course_code].course_name
        if course_name not in self.students[student_id].courses:
            print("Student is not enrolled in this course.")
            return
        try:
            grade = float(input("Enter grade: ")) #Ensuring grade is a valid number
            self.students[student_id].add_grade(course_name, grade)
        except ValueError:
            print("Invalid grade input. Please enter a number.") #Raises error if not a proper grade is inputted
        self.save_data()

        #Saving studnet and course data to CSV files
    def save_data(self):
        with open("students.csv", "w", newline='') as file:
            writer = csv.writer(file)
            for student in self.students.values():
                writer.writerow([student.student_id, student.name, student.courses])
        with open("courses.csv", "w", newline='') as file:
            writer = csv.writer(file)
            for course in self.courses.values():
                writer.writerow([course.course_code, course.course_name])
                
    #Loading studnet and course data to SV fils
    def load_data(self):
        try:
            with open("students.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    student = Student(row[0], row[1])
                    student.courses = eval(row[2])  
                    self.students[row[0]] = student
            with open("courses.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    self.courses[row[0]] = Course(row[0], row[1])
        except FileNotFoundError:
            pass #Ignored if files don't exist
            
#Displays menu to user an handles user input for different opertations
    def menu(self):
        while True:
            print("\nStudent Grading System")
            print("1. Add Student")
            print("2. Add Course")
            print("3. Enroll Student in Course")
            print("4. Add Grade")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.add_course()
            elif choice == "3":
                self.enroll_student()
            elif choice == "4":
                self.add_grade()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    system = StudentGradingSystem()
    system.menu()
