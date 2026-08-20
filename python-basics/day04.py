### *** String, File Handling & Exception Handling *** ###

# **************************
# *** STRING ***
# **************************

## Lower and Upper case:
name = "Aman Kumar"
print(name.upper())
print(name.lower())

## Remove Extra Spaces - strip (only remove the space from start and end)
name = "   Aman Kumar    "
print(name.strip())

## Replace
text = "I love PHP"
# print(text.replace("php", 'python')) ##  X not allowed
print(text.replace("PHP", 'Python')) 

## convert text into list
skills = "python, js, php, laravel, whmcs, rag, react"
text = "I LOVE AI"
# print(skills.split(","))
# print(text.split(" "))
print(text.split(""))



# **************************
# *** FILE HANDLING ***
# **************************

## Write File
with open("notes.txt", "w") as file:
    file.write("Hello Amn..!\nThis File is created with python code.\n***Testing Purpose***\n")


## Read File
with open("notes.txt", "r") as file:
    content = file.read()

print(content)

## Append File
with open("notes.txt", "a") as file:
    file.write("This line from the append file (append file without deleting the existing)")




# **************************
# *** EXCEPTION HANDLING ***
# **************************

try:
    age = int(input("Enter your age: "))
    print(f"Your Age: {age}")
except:
    print("Please enter a number as your age")


try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"Division of {num1}/{num2}: {num1/num2}")
except ValueError:
    print("Enter numbers only")
except ZeroDivisionError:
    print("Number can't be divided by 0")




















