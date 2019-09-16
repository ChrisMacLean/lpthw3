# this just defines the functions and prints some unecessary stuff
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} crackers!")
    print("Man that's enough for a party")
    print("Get a blanket. \n")

# this provides two hardcoded numbers as arguments to the function
print(f"We can just give the functions numbers directly:")
cheese_and_crackers(20, 30)

# this section creates two unrelated variables outside function and then passes these variables as arguments to function
print("Or, we can use variables from our script")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# this does the math
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# this does math plus using script variables from above too
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# can also use input to pass values to functions
cheese_and_crackers(input(f'How much cheese? '),input(f'How many crackers? '))
