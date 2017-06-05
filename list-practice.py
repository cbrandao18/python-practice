import random
allMessages = [ 'It is certain',
                'It is decidedly so',
                'Without a doubt',
                'Yes definitely',
                'You may rely on it',
                'As I see it, yes',
                'Most likely',
                'Outlook good',
                'Yes',
                'Signs point to yes',
                'Reply hazy try again',
                'Ask again later',
                'Better not tell you now',
                'Cannot predict now',
                'Concentrate and ask again',
                'Don\'t count on it',
                'My reply is no',
                'My sources say no',
                'Outlook not so good',
                'Very doubtful' ]

##Separating allMessages list into positive, netural and negative lists

#first 10 messages are positive
allPositive = allMessages[0:10]
#next 5 messages are neutral
allNeutral = allMessages[10:15]
#next 5 are negative
allNegative = allMessages[15:20]

eightMessages = random.sample(allPositive, 4) + random.sample(allNeutral, 2) + random.sample(allNegative, 2)
print random.sample(eightMessages, 1)[0] 
