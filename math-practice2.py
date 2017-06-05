import math

numbers = [5, 8, 27, 34, 71, 6]
n = len(numbers)

def get_sum_avg_std(numbers):
    summation = 0
    
    for num in numbers:
        summation = summation + num

    avg = summation/n

    numerator = 0
    for num in numbers:
        numerator = numerator + (num - avg)**2
    sd = math.sqrt(numerator/(n-1))

    return summation, avg, sd

print get_sum_avg_std(numbers)
