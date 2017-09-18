# Sort the grade and put into another file

# Create a dictionary first

bestStudent = {}
f = open('studentGrade.txt')
for line in f:
    name, grade = line.split()
    # grade -> key  name -> value
    bestStudent[grade] = name
f.close()

bestStudentStr = " "

# Sort the dictionary
for i in sorted(bestStudent.keys(), reverse=True):
    print bestStudent[i] + ' scored a ' + i
    bestStudentStr += bestStudent[i] + ' scored a ' + i + '\n'

    print "\n The best student rank \n\n" + bestStudentStr

outToFile = open('studentRank.txt',  mode='w')
outToFile.write(bestStudentStr)

outToFile.close()