import random
import time

guess_num = random.randint(1,1000)
guess_taken = -1
chances = 0

while chances < 10:
    guess_taken = input('Guess a number between 1 to 1000:\n')
    guess_taken = int(guess_taken)
    chances +=1
    
    if guess_taken < guess_num:
        print("ahh, your guess is low.")
    elif guess_taken > guess_num:
        print('ahh, your guess is high.')
    elif guess_taken == guess_num:
        break

if guess_taken == guess_num:
    chances = str(chances)
    print('YOU WON, YOU TOOK '+chances+' CHANCES.')
elif guess_taken != guess_num:
    guess_num = str(guess_num)
    print('YOU LOSE, THE NUMBER WAS '+guess_num)