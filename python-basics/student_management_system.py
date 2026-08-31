### Student Management System

class Student: 
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def show_details(self):
        print(f"Hi, please find the your profile details here:\nName: {self.name}\nAge: {self.age}\nCourse: {self.course}")
        
        if self.age >= 18:
            print("You are adult")
        else:
            print("You are minor")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
course = input("Enter your course: ")

student = Student(name, age, course)
result = student.show_details()

print(result)