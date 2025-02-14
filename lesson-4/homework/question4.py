import random

def play_game():
    while True:
        number = random.randint(1, 100)
        attempts = 10

        print("\nGuess the number between 1 and 100! You have 10 attempts.")

        for _ in range(attempts):
            try:
                guess = int(input("Enter your guess: "))
                
                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                    continue
                
                if guess > number:
                    print("Too high!")
                elif guess < number:
                    print("Too low!")
                else:
                    print("You guessed it right! 🎉")
                    return

            except ValueError:
                print("Invalid input! Please enter a valid number.")

        print(f"You lost. The correct number was {number}. Want to play again? (Y/YES/ok)")

        again = input().strip().lower()
        if again not in ['y', 'yes', 'ok']:
            print("Thanks for playing! Goodbye!")
            break

play_game()