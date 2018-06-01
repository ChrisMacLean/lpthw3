from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

# readline returns the \n so need the end = "" to stop that if desired
def print_a_line(line_count, f):
    print(line_count, f.readline(), end = "")

current_file = open(input_file)

print("First let's print the whole file:\n")

# this is saying print(test.txt.read(current_file()))
print_all(current_file)

print("Now let's rewind, kind of like a tape.\n")

# this is current_file.seek(0)
rewind(current_file)

print("Let's print 3 lines")

# this makes current line = 1,2,3 respectively then passes to print_a_line function
current_line = 1

current_line += 0
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
