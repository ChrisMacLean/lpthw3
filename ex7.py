print("Mary had a little lamb")
#this condenses the .format empty variable replacement thing from ex6 into 1 line
#instead of replacing with variable though we are replacing it with a literal string of 'snow'
print("It's fleece was white as {}.".format('snow')) # 'snow' is string being put in the brackets
print("And everywhere that Mary went.")
print("." * 10) #what'd that do? This duplicates the literal 10 times

#just makes a ton of variables
end1 = "C"
end2 = "h"
end3 = "e"
end4 = 'e'
end5 = 's'
end6 = 'e'
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'

#watch that comma at the end, try removing it to break syntax
#concatenates the above variables and generates a new one mid print that is the space in Cheese Burger
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
