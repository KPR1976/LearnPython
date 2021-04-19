'''
https://docs.microsoft.com/en-us/learn/modules/python-while/6-challenge-2
Write the code to implement an improved number guessing game
Rebuild the number guessing game, but this time:

Display the current guess number.
If the guess is too low, tell the user "Your guess is too low, try again!"
If the guess is too high, tell the user "Your guess is too high, try again!"
If the user enters a nonnumeric value, tell the user "Numbers only, please!"
Also, take note of the output. The prompts and messages have changed when compared to the original challenge.
No matter how you do it, your code should produce the following output (given the randomly generated answer and the guesses).
'''

import random

value = random.randint(1, 10)
count = 0
guess = 0
print('Guess a number between 1 and 10')
while guess != value:
    count += 1
    guess = input(f'Enter guess #{count}: ')
    if guess.isnumeric():
        guess = int(guess)
        if guess > value:
            print('Your guess is too high, try again!')
        else:
            print('Your guess is too low, try again!')
    else:
        print('Numbers only, please!')
else:
    print(f'You guessed it in {count} tries!')