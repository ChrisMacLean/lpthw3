# this whole exercise doesn't seem that complicated really
# but introduces idea of using functions and return to set variable values
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Lets do some math with functions")

#using the above defined functions to do some simple math
age = add(23, 5)
height = subtract(78, 6)
weight = multiply(108, 2)
iq = divide(100, 2)

print(f"Age: {age}, height: {height}, weight: {weight}, iq: {iq}")

# you can feed it input too
age_input = add(float(input(f'First age number ->')), float(input(f'second age number ->')))

print(f"Those add up to {age_input}")

# OOO test below, nesting shit
# what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
