from sys import argv
# import function form sys 
script, filename = argv
# setting argument

#print some information
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?") # waiting for choise leave or continue

# open a file with write mode
print "Opening the file..."
target = open(filename, 'w') # w mean writing mode

# w mode contain truncate, there are use
'''
# clean file
print "Truncating the file. Goodbye!"
target.truncate() # if file already exists 
'''
print "Now I'm going to ask you for three lines."
# get three lines from user
line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

# writing three lines to file
print "I'm going to write these to the file."
'''
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
'''
writing = line1 + "\n" + line2 + "\n" + line3
target.write(writing)

# close file (saved)
print "And finally, we close it."
target.close()