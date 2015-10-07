from sys import argv

# setting argument and prompt
# script mean .py file
script, user_name = argv
prompt = '>>'

# Starting 
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
# question one
print "Do you like me %s?" % user_name
likes = raw_input(prompt)
# question two
print "Where do you live %s?" % user_name
lives = raw_input(prompt)
# question three
print "What kind of computer do you have?"
computer = raw_input(prompt)

# final result
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives,computer)