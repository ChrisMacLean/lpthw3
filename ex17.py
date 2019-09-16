from sys import argv
from os.path import exists

# so this time we're giving it script name but also providing from and to file variables
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these on 1 line right? indata = open(from_file).read()?
# in_file = open(from_file)
# indata = in_file.read()

#yes you can do it in one line
indata = open(from_file).read()

# these things are really superfluous but just show more info about file
print(f"The input file is {len(indata)} bytes long")
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# this is the part that actually does stuff
# opens file in write mode and writes indata to it
out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, done.")

# don't need to close in_file because it doesn't exist anymore
out_file.close()
# in_file.close()
