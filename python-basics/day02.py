### *** Python functions ***

### Basic function define
def greet():
    print("Hello..!")

# function call
greet()


### Calculator
def calculator(a, b):
    print(f"Adittion: {a} + {b} = {a+b}")
    print(f"Subtraction: {a} - {b} = {a-b}")
    print(f"Multiplication: {a} * {b} = {a*b}")
    print(f"Division: {a} / {b} = {a/b}")
    print(f"Modulus: {a} % {b} = {a%b}")

calculator(10, 9)   


### calculate age 
def age_cal(age):
    years = 2026-age 
    print(f"You are {years} old.")

age = int(input("Enter you birth year: "))
age_cal(age)



### conditions
total = int(input("Enter total marks: "))
marks = int(input("Enter obtained marks: "))

percentage = (marks/total) * 100

if percentage > 33:
    print(f"Your makrs percentage is {percentage}%\nCongradulations! You are Passed.")
else:
    print(f"Your makrs percentage is {percentage}%\nSorry! You are Failed.")


### condition with function

def check_voting_eligibility(year):
    if year <= 2026:
        age = 2026-year
        if age >= 18:
            print(f"Your are {age} years old and eligible for vote") 
        else:
            print(f"Your are {age} years old and not eligible for vote") 
    else:
        print(f"Invalid birth year") 

year = int(input("Enter your birth year: "))
check_voting_eligibility(year)


### Loop
count = 10

for count in range(100):
    print(count)
    count+1


### counting with loop + function

def count_fun(a, b):
    print(f"Counting from {a} to {b}:")
    for num in range(a, b+1):
        print(num)
        num+1


count_fun(10, 15)

### reverse the counting 

def rev_count_fun(num):
    print(f"Reverse counting from {num}:")
    for i in range(num, 0, -1):
        print(i)

num = int(input("Enter a number: "))
rev_count_fun(num)



### Task, print the student manager:

def student_mngr(name, age, course):
    print(f"Welcome {name}")
    print("Please find your details below: ")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Course: {course}")
    if age >= 18:
        print("***You are adult student ***")
    else:
        print("*** You are minor student ***")

name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
course = str(input("Enter your course: "))

student_mngr(name, age, course)

