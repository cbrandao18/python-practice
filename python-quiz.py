#Christie Brandao

##PART 1

#Question 1
# The following expression evalutes to 3 because int uses a string and a number ('3' * 2) which
# evaluates to 33 as it takes '3' twice making it 33. It divides 33 by 11 which is 3. Then in range(10)
# which is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], the expression evalutes the 3rd index which is 3.

#Question 2
def cmpx(x,y):
    greater = 1
    equal = 0
    smaller = -1

    if (x < y):
        return smaller
    elif (x == y):
        return equal
    else :
        return greater
    
print cmpx(10,5)
print cmpx(123,'123')
print cmpx('abc','aac')
print cmpx('abc','abc')

#Question 3
#list_1 = [expr(i) for i in list_0 if func(i)]

#Question 4
print
i=5
print i**+2
# The above expression evalutes to 25. Which is 5 ** 2 or 5 raised to the power of 2. This works because
# there is not a number on the lefthand side of the + so it wouldn't add the numbers.

#Question 5
#In Python 2, True, False, and None are not included in the keyword list, and the following prints all the
# keywords which are all lowercase. So in python2, all keywords are lowercase, but this is not true for python3.
print
import keyword
print keyword.kwlist

#Question 6
print
print [[x, y] for x in range(0, 4) for y in range(0, 4)]
q6list = []
for c in range(0,4):
    for v in range(0,4):
        q6list.append([c,v])
print q6list

#Question 7
print 
i=0
j=0
#To fix the expression, i took away the 'and' and replaced it with 'for'
print [ [i,j] for i in range(0, 10, 2) for j in range(1, 10, 2)]


##PART 2 - Question 8
print
def get2nd(nums):
    numsx = list(set(nums))
    if numsx == []:
        return
    if len(numsx)==1:
        return
    for num in numsx:
        if isinstance(num, (int, long, float)) is False:
            return
    numsx.sort()
    return numsx[len(numsx)-2]

nums = {5, 3, 1, 6, 10}
#Test case 1: The following should print 6
print get2nd(nums)

nums2 = {4, 2, 3, 4, 5, 6, 7, 99}
#Test case 2: The following should print 7
print get2nd(nums2)

nums3 = {}
#Test case 3: The following should print None
print get2nd(nums3)

nums4 = {'string', 1, 3}
#Test case 4: The following should print None
print get2nd(nums4)

##PART 3 - Question 10
print
import sys
sys.path.append('C:\\brandao')
from geom.point import *

def man_distance(p1, p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]

    distx = abs(x1-x2)
    disty = abs(y1-y2)
    dist = distx + disty
    return dist

p1 = Point(-5,9)
p2 = Point(2,6)
print man_distance(p1,p2)
