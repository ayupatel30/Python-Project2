#Ayushi Patel
#Random Number Guessing

#We are using this random import from the Pygame library to get random numbers for game.

import random
import time #Python model that will help us get time so user can get notify when the window will be gone.

number = random.randint(1, 10) #It will get random numbers from 1 to 10

player_name = input("Hello, What's your name?") #Prints out statement asking for their name
number_of_guesses = 0
print('okay! '+ player_name+ ' I am Guessing a number between 1 and 10:')

#While loop is being used to get the variable in range
while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))
    print('Window will be closed in 5 seconds.')
    time.sleep(5) #will close the window in time being.