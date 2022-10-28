import random #import random library

def guess(x): #define a function guess to take the range 
    random_number = random.randint(1,x) #random_number takes random numbers everytime
    guess = 0 #let guess starts from 0
    while guess != random_number: #loop will iterate until the guess becomes equal to random_number
        guess = int(input(f"Guess a number between 1 to {x}: ")) #enter a number between 1 to x until the number is guessed correctly
        if guess < random_number: #if the guessed number is less than the random_number
            print("Sorry. Guess again. Too low")
        elif guess > random_number: #if the guessed number is grater than the random_number
            print("Sorry. Guess number. Too high")
    print(f"Congrats!. You have guessed the number {guess} correctly") 
    
guess(10) # passing the value of x 
