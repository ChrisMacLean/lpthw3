# escape sequences using \ and """

# \t is a tab
tabby_cat = "\tI'm tabbed in."
# \n is new line
persian_cat = "I'm split\non a line."
# \\ is a backslash
backslash_cat = "I'm \\ a \\ cat."
# regular tabs then \n\t to do a new line and tab consecutively
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# just testing out some escape sequences

# print("\\") #backslash
# print("\'") #single quote
# print("\"") #double quote
# print("\a") #ASCII bell
# print("\b") #ASCII backspace
# print("\f") #ASCII formfeed
# print("\n") #ASCII linefeed
# print("\n{name}") #character named name in unicode only?
# print("\r") #carriage return
# print("t") #horizontal tab
# print("\uxxxx") #character with 16-bit hex value
# print("\Uxxxxxxxx") #character with 32-bit hex value
# print("\v") #ASCII vertical tab
# print("\ooo") #character with octal value 000
# print("xhh") #character with hex value hh
