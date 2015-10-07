#assign formatter to variable
formatter = "%r %r %r %r"

# replace formatter with number
print formatter % (1, 2, 3, 4)
# replace formatter with alphabetical nmber
print formatter % ("one", "two", "three", "four")
# replace formatter with bulen values
print formatter % (True, False, False, True)
# replace formatter with formatter
print formatter % (formatter, formatter, formatter, formatter)
# replace formatter with sentence string
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)