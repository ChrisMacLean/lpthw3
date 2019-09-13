cars = 1000
space_in_a_car = 4.0
drivers = 30
passengers = 90
# variables can be derived from other variables
cars_not_driven = cars - drivers # 1000 - 30
cars_driven = drivers # 30
carpool_capacity = cars_driven * space_in_a_car # 30 * 4.0
average_passengers_per_car = passengers / cars_driven # 90 / 30


print('There are', cars, 'cars available.')
print('there are only', drivers, 'drivers available')
print('there will be', cars_not_driven, 'empty cars today')
print('We can transport', carpool_capacity, 'people today')
print('We have', passengers, 'to carpool today')
print('We need to put about', average_passengers_per_car, 'in each car')
