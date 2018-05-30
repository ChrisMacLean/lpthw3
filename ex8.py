#ok so I think this is setting up 4 + in the variable
formatter = "{} {} {} {}"

#the below is all different ways of passing arguments to format function

#this is setting up 4 integers?whole numbers
print(formatter.format(1, 2, 3, 4))
#this sets up literal strings
print(formatter.format("one", "two", "three", "four"))
#this sets up boolean strings
print(formatter.format(True, False, False, True))
#I don't get what this one does just yet, variables?
#so it looks like it spits out variable definition which is just empty brackets
print(formatter.format(formatter, formatter, formatter, formatter))
#this one makes it print multiple lines?
#nope it doesn't make new lines just you can write in multiple lines for ease of use
print(formatter.format(
    "Try your",
    "Own Text Here",
    "Maybe a poem",
    "Or a song about fear"
))
