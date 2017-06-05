import random
"""
A random number is chosen between 0 and 10.
It prints a string saying if the user has guessed the random number in 3 tries.

Input:

    user_in = any value

Output:

    "You got it!"  if they guessed the number within 3 tries
    "Too bad!"     otherwise
    
"""
def pick3():
    random_num = random.randint(0,10)
    i = 0
    while (i < 3):
        user_in = input("Enter your guess for the random number: ")
        if (user_in == random_num):
            print ("You got it!")
            i = 3
        else:
            i = i + 1
            if (i == 3):
                print ("Too bad!")

pick3()
