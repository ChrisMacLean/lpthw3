# print("How old are you?", end=' ')
# age = input()
# print("How tall are you?", end=' ')
# height = input() # was missing the variable for height
# print("How much do you weigh?", end=' ') # was also missing this the closing parentheses
# weight = input()
#
# print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# missing from sys import argv
# from sys import argv
#
# script, filename = argv
#
# txt = open(filename) # filename was mispelled
#
# print(f"Here's your file {filename}:") # was missing the f in front of quotes
# print(txt.read()) # txt variable was mispelled
#
# print("Type the filename again:")
# file_again = input("> ")
#
# txt_again = open(file_again)
#
# # txt_again_read is not a defined function, changed to txt_again.read
# print(txt_again.read())


# print('Let\'s practice everything.') # missing the quote escape in let's
# # was missing multiline quotes
# print('''You\'d need to know \'bout escapes
#       with \\ that do \n newlines and \t tabs.''')
#
# poem = """
# \tThe lovely world
# with logic so firmly planted
# cannot discern \n the needs of love
# nor comprehend passion from intuition
# and requires an explanation
# \n\t\twhere there is none.
# """
# # missing quotes around things
# print("--------------")
# print(poem)
# print("--------------")


# five = 10 - (2 + 3) # removed extra minus and fixed OOP
# print(f"This should be five: {five}") # missing closing parentheses
#
# def secret_formula(started) : # missing the colon in define syntax
#     jelly_beans = started * 500
#     jars = jelly_beans / 1000
#     crates = jars / 100 # had no math operator
#     return jelly_beans, jars, crates
#
#
# start_point = 10000
# beans, jars, crates = secret_formula(start_point) # missing 3rd variable from function def
#
# # remember that this is another way to format a string
# print("With a starting point of: {}".format(start_point))
# # it's just like with an f"" string
# print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")
#
# start_point = start_point / 10
#
# print("We can also do that this way:")
# formula = secret_formula(start_point) #start_point variable was mispelled
# # this is an easy way to apply a list to a format string
# print("We'd have {} beans, {} jars, and {} crates.".format(*formula)) # this only works because we have 3 {} for the 3 things returned by formula


people = 20
cats = 30 # was misspelled compared to later
dogs = 15


if people < cats:
    print ("Too many cats! The world is doomed!")

if people > cats: # same check as above but differen text
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs: # missing colon
    print("The world is dry!")

# saying dogs = 15 + 5 because we assigned it a value of 15 above
dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs: # missing the colon again
    print("People are less than or equal to dogs.") # missing end quotes

if people == dogs: # cannot use = in value compare, use ==
    print("People are dogs.")
