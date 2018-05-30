#this sets a variable and then puts it inside another one as a string component
types_of_people = 10
x = f"There are {types_of_people} types of people."

# same as above basically
binary = "binary"
do_not = "don't" #if using single quotes would have to escape the don't apostrophe?
y = f"Those who know {binary} and those who {do_not}."

#setting these above makes print easier and shorter by just calling variables
print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

#I think this sets up a string with a blank variable spot "reserved"
hilarious = False #case matters, needed to be capital F
joke_evaluation = "Isn't that joke so funny?! {}"

#I think this format() puts the hilarious variable in the "reserved" spot from above
#also a different way of formatting instead of f""
print(joke_evaluation.format(hilarious))

#this does nothing because binary has no blank variable spot?
print(binary.format(do_not))

#this should do something because it does have blank variable spot?
print(joke_evaluation.format(binary))

w = "This is the left side of..."
e = "a string with a right side."

#This concatenates strings into 1 line
print(w + e)
