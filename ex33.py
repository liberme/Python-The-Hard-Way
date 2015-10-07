'''
i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
	
	i = i + 1
	print "Number now: ", numbers
	print "At the bottom i is %d" % i
	
	
print "The numbers: "

for num in numbers:
	print num	
	
def while_loop(times, scale): # become function
	i = 0
	numbers = []
	
	while i < times:
		print "At the top i is %d" % i
		numbers.append(i)
		
		i = i + scale
		print "Number now: ", numbers
		print "At the bottom i is %d" % i
		
	print "The numbers: "
	
	for num in numbers:
		print num
		
# Study drill 4 Rewrite the script again to
# use this function to see what effect that has.
while_loop(6, 1)
'''
# Study drill 5 rewrite it to use for-loops and range. 
# Do you need the incrementor in the middle anymore? 
# What happens if you do not get rid of it?
numbers = []

for i in range(0, 6):
	print "At the top i is %d" % i
	numbers.append(i)
	
	i = i + 1 #In for-loop, this is no need

	print "Number now: ", numbers
	print "At the bottom i is %d" % i

print "The numbers"

for num in numbers:
	print num
	