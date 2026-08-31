# ### -------------- OOPS CONCEPTS --------------

##
# class Student:
#     pass

# student1 = Student()
# student2 = Student()

# print(student1)
# print(student2)

# #
# class Student:
#     name = "Amn"
#     age = 22
#     course = "Python"

# student = Student()
# print(student.name)
# print(student.age)
# print(student.course)


# constructor __init__

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def greet(self):
#         print(f"Hello {self.name} welcome..!")

# person = Person("Amn", 22)
# print(person.name) 
# print(person.age)

# print(person.greet()) 



### doc word count

class Document:
    def __init__(self, filename):
        self.filename = filename
    
    def word_count(self):
        ## read file
        with open(self.filename, "r") as file:
            content = file.read()
        print(f"File content is: {content}")
        print(f"Length: {len(content.split())}")

## first create and write file
with open("test.txt", "w") as file:
    file.write("Hi, I am Aman Kumar.\nI am a PHP developer but working with python to become an AI Engineer.\nThanks!") 


doc = Document("test.txt")
print(doc.word_count())