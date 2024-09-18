import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")
    
    while True:
        guess = int(input("Enter your guess: "))
        
        attempts += 1
        
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break


guessing_game()
