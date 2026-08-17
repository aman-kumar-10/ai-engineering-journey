from datetime import date

name = "Aman Kumar"
age = 21
dob = {
    "day": 10,
    "month": 7,
    "year": 2004
}
profile = "PHP Developer"
height = 5.9
city = "Mohali"

today = date.today()

print("------- User Profile -------")
print(f"Name: {name}")
print(f"DOB: {dob["day"]}/{dob["month"]}/{dob["year"]}")
print(f"Profile: {profile}")
print(f"Height: {height}")
print(f"City: {city}")
print(f"Created on: {today}")
print("------- Thanks! -------")