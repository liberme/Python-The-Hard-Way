#define a function to deal with two number's adding
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
# define a function to subtract
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
# define a function to multiply
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
# define a function to divide
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	
print "Let's do some math with just functions!"

# assign values to variable by calling functions 
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what , "Can you do it by hand?"

print "There are another puzzle."

which = subtract(age, subtract(age, divide(iq, weight)))

print " There result is : %d" % which