### TASK ###
#  - take user input as notes, 
#  - create a file and then write that notes in that file.
#  - then read that file
#  - replace the things from the file and add new content then also read again.

# user input
name = input("Enter your name: ")
name = name.strip()
name = name.upper()

notes = input("Please write your notes here: ")
notes = name + "\n" + notes
# remove extra spces if have
notes = notes.strip()

# create a file and write the notes
with open("practice_sample.txt", "w") as file:
    file.write(notes)

# read file
with open("practice_sample.txt", "r") as file:
    content = file.read()
print(content)

replace_from = input("Enter the text you want to replace from: ")
replace_with = input("Enter the text you want to replace with: ")

# replace
updated_content = content.replace(replace_from, replace_with) 
with open("practice_sample.txt", "w") as file:
    file.write(updated_content)

# read again updated
with open("practice_sample.txt", "r") as file:
    updatedfile = file.read()
print(updatedfile)

# append new items
append = input("Please enter new notes content to append: ")
with open("practice_sample.txt", "a") as file:
    file.write("\n" + append)

# Final Content
with open("practice_sample.txt", "r") as file:
    final_content = file.read()
print(final_content)
