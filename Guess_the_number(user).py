import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"is {guess} too high(h), too low(l), or correct (c): ")
        if feedback == 'h':  
            guess = guess-1
        elif feedback == 'l':
            guess = guess+1
    print(f"Yay! Computer guessed the number {guess} correctly!")
computer_guess(20)

