# this one is like scripts with argv
# must be inside parentheses to work
# colon then indents, first indented line unpacks arguments
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# dont actually need *args to unpack, can just put names right in def
def print_two_again(arg1,arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#  just 1 argument
def print_one(arg1):
    print(f"arg1 {arg1}.")

# no arguments
def print_none():
    print("I got nothing.")

print_two("Chris","Maclean")
print_two_again("Chris","Maclean")
print_one("First!")
print_none()
