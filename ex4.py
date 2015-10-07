cars = 100 # assign variables 'cars' equal to 100
space_in_a_car = 4 # assign  variables 'space_in_a_car' equal to 4.0
drivers = 30 # assign variables 'drivers' equal to 30
passengers = 90 # assign variables 'passengers' equal to 90
cars_not_driven = cars - drivers # assign variables 'cars_not_driven' equal to cars subtract dirvers
cars_driven = drivers # assign cars_driven equal to driversvers
carpool_capacity = cars_driven * space_in_a_car # assign carpool_capacity equal to  car_driven multiply space_in_a_car
average_passengers_per_car = passengers / cars_driven # assign average_passengers_per_car equal to passengers divide car_driven

# then print the result
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car."
