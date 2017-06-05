i=0
summation = 0
while (i<3):
    if (i==0):
        print "Nogerof the Wizard: Give me your first number"
    if (i==1):
        print "Nogerof the Wizard: Give me your second number"
    if (i==2):
        print "Nogerof the Wizard: Give me your third number"
    keyboard_in = input()
    summation = summation + keyboard_in

    if (summation%2 == 0):
        print "The sum is even"
    else:
        print "The sum is odd"
    i = i+1
