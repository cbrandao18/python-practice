def amt_of_change(cost, paid):
    change = paid - cost
    amt_20 = 0
    amt_10 = 0
    amt_5 = 0
    amt_2 = 0
    amt_1 = 0
    if (change / 20 > 0):
        amt_20 = change/20
        change = change - 20*amt_20
    if (change / 10 > 0):
        amt_10 = change/10
        change = change - 10*amt_10
    if (change / 5 > 0):
        amt_5 = change/5
        change = change - 5*amt_5
    if (change / 2 > 0):
        amt_2 = change/2
        change = change - 2*amt_2
    if (change / 1 > 0):
        amt_1 = change/1
        change = change - amt_1

    print "The following change is given: " + str(amt_20) + " $20 bills, " + str(amt_10) + " $10 bills, " + str(amt_5) + " $5 bills, " + str(amt_2) + " $2 bills, " + str(amt_1) + " $1 bills. " 
    
amt_of_change(20,43)
