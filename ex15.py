# bring in argv modeul
from sys import argv

# argument is filename to be read
script, filename = argv

# this variable is open function on filename, default open is to read from file
txt = open(filename)

# this just prints the value given to argv in command prompt, should be ex15_sample.txt
print(f"Here's your file {filename}:")
# this is a read command with no parameters, so it's just reading everything
# I assume you can only do .read on an already opened file
print(txt.read())
#important to close after opening
txt.close()

# this is functionally the same as above just not using argv but input instead
print("Type the filename again:")
# instead of argv using input to get file name
file_again = input("> ")

# this variable just performs open on the previous variable
txt_again = open(file_again)

# this prints the results of the read function being used on the variable
print(txt_again.read())
# close after opening
txt_again.close()
