import math

import decimal

x, y, z = 1, 2, 3.3
print (x, y, z)

#Function

def boolfunc(a, b):

    print(type(a))
    # if a and b both true, then print true
    # False
    print(a and b)
    # True
    print(a or b)
    # True
    print(not b)

boolfunc(True, False)

def intFunc():
    a = 5
    b = 2
    print "a + b = ", a+b
    print '{0} + {1} ='.format(a, b), a+b

    print '{0} - {1} ='.format(a, b), a-b
    print '{0} ** {1} ='.format(a,b), a**b

    print "Binary format for 4 ", bin(4)
    print float(a)
    print pow(x,y)
    #
    print round(z,3)
    print math.ceil(z)
    print math.floor(z)

    c = 1.24242491134341111
    # 1.24242491134
    # By using decimal, no matter how many decimals we have, it
    # will print all of it
    c = decimal.Decimal("1.24242491134341111")
    print(c)



intFunc()
