import random

def play_game():
    print("\n------------------ INTERACTIVE GUESSING GAME ---------------------")
    print("Choose a difficulty level:")
    print("1. Easy (unlimited attempts)")
    print("2. Normal (10 attempts)")
    print("3. Hard (7 attempts, guess TWO numbers)")
    choice = input("Choice: ").lower()
    score = 0
    attempts = 0

    # Easy Mode
    if choice in ["1", "easy"]:
        max_range = int(input("Enter maximum range: "))
        number = random.randint(0, max_range)
        print(f"Guess the number between 0 and {max_range}!")
    
        # Guessing Starts
        while True:
            guess = int(input("Your guess: "))
            attempts += 1
            if guess == number:
                print(f"Correct! You guessed it in {attempts} tries.")
                score += max(100 - (attempts * 5), 10)
                break
            elif abs(guess - number) <= 2:
                print("Very close!")
            elif abs(guess - number) <= 5:
                print("Close!")
            elif guess < number:
                print("Much too low!")
            else:
                print("⬇Much too high!")

    # Normal Mode
    elif choice in ["2", "normal"]:
        max_range = int(input("Enter maximum range: "))
        number = random.randint(0, max_range)
        print(f"Guess the number between 0 and {max_range}! You have 10 attempts.")

        # Guessing Starts
        max_attempts = 10
        while attempts < max_attempts:
            guess = int(input(f"Attempt {attempts+1}: "))
            attempts += 1
            
            if guess == number:
                print(f"Correct! You guessed it in {attempts} tries.")
                score += max(150 - (attempts * 10), 20)
                break
            elif abs(guess - number) <= 2:
                print("Very close!")
            elif abs(guess - number) <= 5:
                print("Close!")
            elif guess < number:
                print("Much too low!")
            else:
                print("Much too high!")
        else:
            print(f"Out of attempts! The number was {number}.")

    # Hard Mode
    elif choice in ["3", "hard"]:
        max_range = int(input("Enter maximum range: "))
        number = random.randint(0, max_range)
        print(f"Guess TWO numbers between 0 and {max_range}! You have 7 attempts.")

        # Guessing starts
        max_attempts = 7
        while attempts < max_attempts:
            guess = int(input("Enter first guess: "))
            attempts += 1
            if guess == number:
                print(f"Correct! You guessed it in {attempts} tries.")
                score += max(150 - (attempts * 10), 20)
                break
            elif abs(guess - number) <= 2:
                print("Very close!")
            elif abs(guess - number) <= 5:
                print("Close!")
            elif guess < number:
                print("Much too low!")
            else:
                print("Much too high!")
        else:
            print(f"Out of attempts! The number was {number}.")

    else:
        print("Invalid choice!")
        return 0

    return score


# Game Loop with Replay
total_score = 0
while True:
    score = play_game()
    total_score += score
    print(f"Your score this round: {score}")
    print(f"Your total score: {total_score}")

    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing! Final Score:", total_score)
        break
