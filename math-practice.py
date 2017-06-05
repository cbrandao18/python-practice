import math

numbers = [5, 8, 27, 34, 71, 6]
n = len(numbers)

def getSum(numbers):
    summation = 0
    for num in numbers:
        summation = summation + num
    return summation

def getSD(numbers):
    avg = getSum(numbers)/n
    numerator = 0
    for num in numbers:
        numerator = numerator + (num - avg)**2
    sd = math.sqrt(numerator/(n-1))
    return sd

print "The sum of the numbers is "+ str(getSum(numbers))
print "The average of the numbers is "+ str(getSum(numbers)/n)
print "The standard deviation of the numbers is "+ str(getSD(numbers))

