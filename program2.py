#Second app - Guess that number game.
import random

print ('----------------------------')
print ('----GUESS THAT NUMBER GAME--')
print ('----------------------------')
#Create extra line
print()

the_number = random.randint(0,100)
#Initialize guess variable to something outside the random initializer
guess = -1
name = input('Player what is your name? ')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print ('Sorry {0}, your guess of {1} was too low.'.format(name, guess))
    elif guess > the_number:
        print('Sorry {0}, your guess of {1} was too high.'.format(name, guess))
    else:
        print('Nice job {0}! You won.'.format(name))

print('done')
