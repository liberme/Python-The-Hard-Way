from sys import argv # import function from sys module

script, filename = argv
# line 1 to 3 uses argv to get filename
txt = open(filename) # here open file

print "Here are your file %r:" % filename # little message
print txt.read() # read file
txt.close() # added after stduy drill
print "Type the filename again:" # message again
file_again = raw_input("> ") # got filename from user type

txt_again = open(file_again) # open file

print txt_again.read() # read file and print it
txt_again.close() # added after stduy drill

# There are two way to get filename
# 1. argv
# 2. raw_input