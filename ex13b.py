# this whole thing is part of study drill for ex13, combine input and argv
from sys import argv

script = argv
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

print("The script is named: ", script)
print(f"So your full name is {first_name} {last_name}.")
