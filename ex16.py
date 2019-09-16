from sys import argv

script, filename = argv

# ok so ctrl-c is keyboard interrupt, other wise it opens and truncates it
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# really this input only allows ctrl-c interrupt, anything else and it continues
input("?")

# this opens the file with a write paramter "w" so we can write to it later
print("Opening the file...")
target = open(filename, "w")

# This truncate is unecessary, truncates when doing open in write mode
# since we already opened the file does target know it's the currently open file?
print("Truncating the file. Goodbye!")
target.truncate

print("Now I'm going to ask you for three lines.")
# now we are providing input for these 3 variables
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
# this takes input and writes it to files with line breaks to make it 3 lines long
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
target.write(f"{line1}\n{line2}\n{line3}")

print("And finally, we close it.")
target.close


# read related functions
# close - like saving
# read - reads the whole file
# readline - reads just one line
# truncate - empties the file
# write('stuff') - writes stuff to the file
# seek(0) - move the read/write to the beginning of file
