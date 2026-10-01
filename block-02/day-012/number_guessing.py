from random import randint

LOGO = r'''
  _______                             __   __              ______                 __
 |   _   .--.--.-----.-----.-----.   |  |_|  |--.-----.   |   _  \.--.--.--------|  |--.-----.----.
 |.  |___|  |  |  -__|__ --|__ --|   |   _|     |  -__|   |.  |   |  |  |        |  _  |  -__|   _|
 |.  |   |_____|_____|_____|_____|   |____|__|__|_____|   |.  |   |_____|__|__|__|_____|_____|__|
 |:  1   |                                                |:  |   |
 |::.. . |                                                |::.|   |
 `-------'                                                `--- ---'
'''
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_answer, turns):
    """Check the user's guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}.")

def set_difficulty():
    """Set the level of diffulty, returns the total number of turns."""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    total_turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {total_turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        total_turns = check_answer(guess, answer, total_turns)
        if total_turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

print(LOGO)
print("Welcome to the Number Guessing Game!")
game()