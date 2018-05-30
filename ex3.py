print("I will now count my chickens")

print("Hens", 25 + 30 / 6)# division takes precedence over addition
print("Roosters", 100 - 25 * 3 % 4)# is it 75 % 4 or 25 *(3 % 4)?

# forget "regular" decimal long division when using modulo?
print("3 % 4:",3 % 4)# remainder of 3
print('25 * 3 % 4:', 25 * 3 % 4)# see next line
print('75 % 4:', 75 % 4)# 75 / 4 = 18 with a REMAINDER of 3. IE 4 * 18 = 72 which is 3 off of 75

print("Now I will count the eggs:")

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6) # aka (1 + 0 - .25 + 6)

print("Is it true that 3 + 2 < 5 - 7?")

print(3 + 2 < 5 - 7) # spits out true/false results with equal operators?

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's false")

print("How about some more")

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or queal?", 5 <= -2)
