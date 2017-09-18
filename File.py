# Pulling the info from file to screen

f = open('studentGrade.txt')
for line in f:
    print line

f.close()

# Print out the best grade

bestGrade = 0
f = open('studentGrade.txt')
for line in f:
    name, grade = line.split()
    if int(grade) > bestGrade:
        bestGrade = int(grade)
        bestStudent = name

print ("\n")

print "Best Grade", bestGrade
print "Best Student", bestStudent
f.close()

