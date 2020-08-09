import random
import time
 
min = 1
max = 6

def dice():
    dice01 = 'y'
    dice_number = input('How many dice you want 1 or 2 ?')
    if dice_number=='1' :
        while dice01=='y' or  dice01 == "yes" :
            print('Rolling dice...')
            time.sleep(0.5)
            print(random.randint(min,max))
            dice01 = input('do you want to roll the  dice again?y/n')
            dice01 = dice01.lower()
            if dice01 == "N" or dice01 == "n":
                print("ok then!")
    elif dice_number=='2':
         while dice01=='y' or dice01 == "Y" or dice01 == "yes" :
            print('Rolling dice...')
            time.sleep(0.52)
            print(random.randint(min,max))
            print(random.randint(min,max))
            dice01 = input('do you want to roll the dice again2?y/n')
            dice01 = dice01.lower()
            if dice01 == "no" or dice01 == "n":
                print("ok then!")

dice()
