import random

def game():
    # Code for Number guessing game
    number_to_guess = random.randint(1, 100)
    guesses = 0
    print("\nStarting a new game...")

    while True:
        try:
            guess_input = input("Enter your guess (1-100) or type 0 to give up: ")
            
            # Code for quitting
            if guess_input == '0':
                print(f"You gave up. The number was {number_to_guess}. 😔")
                return "loss"

            guess = int(guess_input)
            guesses += 1
            
            #Code for hint on 4th guess
            if guess != number_to_guess:
                if guesses == 4:
                    if number_to_guess % 2 == 0:
                        print("Hint: The secret number is even.")
                    else:
                        print("Hint: The secret number is odd.")

                # More hints
                if guess < number_to_guess:
                    difference = number_to_guess - guess
                    if difference <= 10:
                        print("You're very close! Guess a bit higher.")
                    elif difference <= 30:
                        print("You're close, guess a higher number.")
                    else:
                        print("You're far. Guess a higher number.")
                else:  # guess > number_to_guess
                    difference = guess - number_to_guess
                    if difference <= 10:
                        print("You're very close! Guess a bit lower.")
                    elif difference <= 30:
                        print("You're close, guess a lower number.")
                    else:
                        print("You're far. Guess a lower number.")
            else:
                print(f"You guessed the number {number_to_guess} in {guesses} guesses! 🎉")
                return "win"
                
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def play_again():
    """
    Manages the game loop, allowing the player to play multiple rounds.
    Also displays the welcome message and instructions.
    """
    wins = 0
    losses = 0

    print("\n\n\t\tWelcome to the Number Guessing Game! 🧠")
    print("-------------------------------------------------------")
    print("Instructions:")
    print("1. A random number between 1 and 100 has been chosen.")
    print("2. Try to guess the number. The game will give you hints.")
    print("3. On your 4th guess, you'll get a hint about whether the number is even or odd.")
    print("4. You can type 0 at any time to give up.")
    print("-------------------------------------------------------")
    
    while True:
        result = game()
        if result == "win":
            wins += 1
        elif result == "loss":
            losses += 1
        
        print(f"\nCurrent Score: Wins: {wins}, Losses: {losses}")
        
        play_again_input = input("\nDo you want to play again? (y/n): ").lower()
        if play_again_input != 'y':
            print("Thanks for playing! Goodbye. 👋")
            break

# Start the game
play_again()
