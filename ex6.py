# assign string to variables
x = "There are %d types of people." % 10 # replace %d with 10
binary = "binary"
do_not = "don't"
# replace two %s with binary and do_not
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

# alternative way for string formatting
hilarious = False
# write %r within string but not assign value to this %r
joke_evaluation = "Isn't that joke so funny?! %r"

# then we assign value to that in print function
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side"

# just add two variables together
print w + e