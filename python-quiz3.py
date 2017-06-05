##Christie Brandao 
##Question 1
R2D2 = 'a robot'
print R2D2
##The '&' operator is not allowed in variable names. The above is the fixed code.

##Question 2
my_value = 0
for i in range(10):
    my_value = my_value + (11*i)
print float(my_value/10.0)
#The mean is 49.5

##Question 3
sentence = "fox is jumping over another fox that turns out to be a lynx. Or is that an oblex or oryx?"
li = []
for i in range(len(sentence)):
    if sentence[i] == 'o':
        li.append(sentence[i])
print li

##Question 4
a = 10
if a == 10:
    print 'yes'
else:
    print 'no'
#Needed a '==' for comparison instead of '=' which assigns values

##Question 5
print 'I can eat ' + str(20) + ' apples a day!'
#Need to be consistent with quotation marks. The above is the correct code.

##Question 6
nums = [1, 2, 3, 4, 5, 6, 7]
print nums[3:100]
#Yes, the above works and is a valid expression.
#The result returns the number in the 3rd index all the way until the end of the list
#even though there aren't 100 numbers in the list.

##Question 7
tri_num = []
for i in range(1, 10):
    tri_num.append(i*(i+1)//2)
print tri_num

list_comp = [x*(x+1)//2 for x in range(1, 10)]
print list_comp

##Part 2 - Question 10
def diff_chars(string1, string2):
    diff_char_list = []
    string1_len = len(string1)
    string2_len = len(string2)
    i = 0
    j = 0
    while i < string1_len:
        if string1[i] not in string2:
            diff_char_list.append(string1[i])
        i = i + 1
    while j < string2_len:
        if string2[j] not in string1:
            if string2[j] not in diff_char_list:
                diff_char_list.append(string2[j])
        j = j + 1
        
    return diff_char_list
print diff_chars('abcdefg', 'define')

##Part 3 - Question 11
def deg2dms(degree):
    degree_floored = int(degree)
    remainder = degree - degree_floored
    minute_dec = remainder * 60
    minute = int(minute_dec)
    minute_remainder = minute_dec - minute
    seconds = int(round(minute_remainder*60))
    print str(degree_floored) + " " + str(minute) + " " + str(seconds)
deg2dms(13.388)
