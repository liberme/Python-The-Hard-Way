#define a function call cheese_and_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheese!" % cheese_count
	print "You have %d crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"
# use the function with number argument
print "We can just give a function number directly:"
cheese_and_crackers(20, 30)
# use the function with variables argument
print "OR, we can use variables from out script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# use the function with argument with math inside
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# combine variables and math to use function
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
