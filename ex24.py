# this blurb is about escapes like for single quotes needed in the string as literals
print("Let's practice everything")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs')

# this just plays around with some spacers
# reminder triple quotes is multi line string
poem = """
\t the lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
print("----------------")
print(poem)
print("----------------")

# simple addition in a variable
five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

# simple functions define
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
#variable name jelly_beans is temporary within function and so we can just say beans here to hold the return value
# also I think the terms can be on either side of the =
beans, jars, crates = secret_formula(start_point)

#this is another way to format a string
print("With a starting point of: {}".format(start_point))
#it's just like with and f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} creates.".format(*formula))
