
# Tuple-> immutable List!

# The location of 1 and 2 in memory keeps changing, it is mutable
intOne =1
print id(intOne)

intTwo = 2
print id(intTwo)

# dictoinary key, value

dictExample = {"Age" : 33, "Height":"5.2", "Weight": 46}
print dictExample

# Key
print dictExample.get("Age")

# output: [('Age', 33), ('Weight', 46), ('Height', '5.2'
print dictExample.items()

# output: [33, 46, '5.2']
print dictExample.values()

# remove from dictionary
dictExample.pop("Height")
print dictExample

a, b = 2, 9

while a<b:
    print a
    a += 1

for x in [1, 2, 3, 4]:
    print x

# Initial listCycle
listCycle = [1, 2, 3, 4]
# Looping from 1 -- 200
listCycle[:] = range(1, 201)

for i in listCycle:
    print i

# print out the even nums
for i in listCycle:
    if (i%2 == 0):
        continue
    elif (i == 101):
        break
    else:
        print i


