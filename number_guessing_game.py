## Number Guessing Game

import random

secret_number = random.randint(1, 10)
guess_count = 0
guess_limit = 5

def guess_game(secret, count, limit):
    while count < limit:
        guess = input('Guess: ')
        try:
            guess = int(guess)
        except ValueError:
            print('Please enter a number')
            continue
        count += 1
        if guess == secret:
            print('You won!')
            break
        elif count == limit:
            print('You lost!')
            break
        elif guess == "":
            print('Please enter a number')


guess_game(secret_number, guess_count, guess_limit)