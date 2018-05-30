name = "Chris A. MacLean"
age = 28 #for Now
height = 72 # inches
weight = 215 #lbs
eyes = 'blue'
teeth = 'white'
hair = 'brown' # and some grays

#imperial to metric conversions
in_to_cm = 2.54
lb_to_kg = 0.45

#use the above to convert to metric value variables
height_cm = height * in_to_cm
weight_kg = weight * lb_to_kg

#f inside of print tells it to format the variables
print(f"Let's talk about {name}.") #forgot to close quotes
print(f"He's {height} inches tall or {height_cm} centimeters tall.")
print(f"He's {weight} pounds heavy or {weight_kg} kilograms heavy")
print(f"Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth}.")

#this one is tricky on purpose
total = age + height + weight #you can add variables to make a new one
print(f"If I add {age}, {height}, and {weight} I get {total}.")
