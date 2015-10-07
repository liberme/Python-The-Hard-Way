from sys import argv

script, filename = argv
 
print "Now you filename: %r" % filename
print "Opening file"
file = open(filename)

print file.read()
file.close()