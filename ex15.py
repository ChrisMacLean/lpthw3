# bring in argv
from sys import argv

# argument is filename to be read
script, filename = argv

# this variable is open function on filename, default open is to read from file
txt = open(filename)

# this just prints the value given to argv in command prompt, should be ex15_sample.txt
print(f"Here's your file {filename}:")
# this is a read command with no parameters, so it's just reading everything I guess
# I assume you can only do .read on an already opened file
print(txt.read())
#important to close after opening
txt.close()

# this is functionally the same as above just not using argv but input instead
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
# close after opening
txt_again.close()
