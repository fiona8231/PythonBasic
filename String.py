

var = "This is the sample string"
print var

numOne = 2
wordOne = "cats"
# two way to print string
print 'I have {0} {1}'.format(numOne, wordOne)

combineStr = "I have " + str(numOne)+ " " + wordOne
print combineStr

combineStr += " I think? "
print combineStr

stringVar2 = "Just another string"

for i in stringVar2:
   print i
print "\n the first element is", stringVar2[0]

# print all the letters in the same line, as for automatically create a new line.

'''for i in stringVar2:
    print(i, end= " ")'''

for x in range(1, 11):
    # d ->the space between 2 letters
    print '{0:2d} {1:3d} {2:6d}'.format(x, x*x, x*x*x)

print "\n"
string4 = "This is a very cute and smart cat"
print string4.find('cute')
print string4[15:19]

# replace
string4 = string4.replace('a', '2')
print string4

# get rid of the white space
string5 = '              There is bunch of white space here'
print string5

string5 = string5.strip()
print string5

# Split
# output: ['There', 'is', 'bunch', 'of', 'white', 'space', 'here']
string5 = string5.split()
print string5

# output: <type 'list'>
print type(string5)

# Join
# output:There * is * bunch * of * white * space * here
string5 = ' * '.join(string5)
print string5

# Length of the string
print len(string5)

# Raw text, adding r at the beginning
# not going to print new line
# output: I don't want to \n
string6 = r"I don't want to \n"
print string6


