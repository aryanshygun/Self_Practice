import random

def guess(x):
    ran_num=random.randint(1,x)
    guess=0
    while guess!=ran_num:
        guess=int(input(f"enter a number between 1 and {x}:\n"))
        if ran_num > guess:
            print('sorry, your guess is too low!')
        elif ran_num < guess:
            print('sorry, your guess is too high!')
    print(f"congrats, you guessed the correct number which is {guess}")
    
x = random.randint(2,1000)
guess(x)