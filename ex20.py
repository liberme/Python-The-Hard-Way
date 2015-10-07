# import function from sys
from sys import argv
# assing argument
script, input_file = argv
# define functions
def print_all(f): # a function print it read
	print f.read()
	
def rewind(f): # a function to change read position back to start of file
	f.seek(0) # for the second read
	
def print_a_line(line_count, f): # print one line each run time
	print line_count, f.readline()

# open file with filename input_file
current_file = open(input_file)

print "First let's print the whole file:\n"
# use function with current_file argument
print_all(current_file)

print "Now let's rewin, kind of like tape."

# use rewind function back to top
rewind(current_file)

print "Let's print three lines:"
# print line and show number
current_line = 1
print_a_line(current_line, current_file)
# print next line and show number
current_line += 1
print_a_line(current_line, current_file)
# print next line and show number
current_line += 1
print_a_line(current_line, current_file)