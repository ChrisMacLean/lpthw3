# argv is argument variable
from sys import argv
# read the wyss section for how to run this
# this unpacks argv and assigns it to the 4 variables below
# number of arguments has to equal number of variables defined here
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your thrid variable is:", third)

#ok so the .py file im invoking is the 1st variable, 4 total
