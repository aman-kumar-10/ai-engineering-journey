### LISTS
 ## It store multiple values in order, in a single variable

technologies = ["python", "javascript", "FastAPI", "Git"]

print(technologies)
print(technologies[3])
technologies[2] = "react"
print(technologies)
technologies.append("RAG")
print(technologies)

## Loop
for tech in technologies:
    print(tech)


## practice **************************************
users = ["Amn", "Ramit", "Manu", "Rahul", "Ram"]
num = 1

for user in users:
    print(f"{num}: {user}")
    num += 1

## LIST ************************************** END



### * DICTIONARY
 ## similar to list but stores in key->value pair

developer = {
    "name": "Amn",
    "role": "Applied AI Engineer",
    "experience": 2.5,
    "package": "35 LPA",
}

print(developer)
print(developer['role'])
developer['package'] = "45 LPA"
print(developer['package'])

## practice **************************************
student = {
    "name": "Amn",
    "age": 22,
    "course": "AI Engineering",
    "city": "Mohali",
}

for key, value in student.items():
    print(f"{key}: {value}")

## DICTIONARY ************************************** END



### * TUPLE
 ## Similar to the lists but values can not be changed 

numbers = (10, 20, 50, 90)

print(numbers)
print(numbers[2])

numbers[0] = 15 ## not allowed
print(numbers)


## TUPLE ************************************** END



### * SETS
 ## values will be unique

cars = {"Range", "Audi", "BMW", "Audi", "Nano"}

print(cars)

tags = ["AI", "Python", "PHP", "AI", "Python"]
unique_tags = set(tags)
print(tags)
print(unique_tags)

## SETS ************************************** END


### LIST - COMPREHENSIONS
 ## 

numbers = [i for i in range(1, 9)]
print(numbers)

words = ["AI", "FASTAPI", "PYTHON"]
lowercase = [word.lower() for word in words]
print(lowercase)

## practice **************************************
even_number = [i for i in range(1, 10) if i%2 == 0]
print(even_number)

## LIST - COMPREHENSIONS ************************************** END

