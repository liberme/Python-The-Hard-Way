# study drills ex19
def say_myname_many_times(times, name):
	print ("your name is %r \n" % name) * times
# first	
say_myname_many_times(1, 'John')
# second
number = 2
name = 'John'
say_myname_many_times(number, name)
#thrid
say_myname_many_times(number + 1, name)
#fourth
say_myname_many_times(2 + 1 , name)
#fifth
say_myname_many_times(number + number, 'can')
#sixth
say_myname_many_times(len(str(number)), 'Jogn')
#seventh
number = raw_input("Please enter number")
name = raw_input("Please enter your name")
say_myname_many_times(number, name)
#eighth

