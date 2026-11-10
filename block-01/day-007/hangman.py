import random

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ('''
ant baboon badger bat bear beaver camel cat clam cobra cougar
coyote crow deer dog donkey duck eagle ferret fox frog goat
goose hawk lion lizard llama mole monkey moose mouse mule newt
otter owl panda parrot pigeon python rabbit ram rat raven
rhino salmon seal shark sheep skunk sloth snake spider
stork swan tiger toad trout turkey turtle weasel whale wolf
wombat zebra ''').split()

errors = 0
chosen_word = random.choice(word_list).lower()

print("\nWelcome to Hangman game. Are you ready to guess the word?")

# Display blank spaces to guess
placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed '{guess}'.")

    # Display the guess letter in the right positions
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(f"Word to guess: {display}")

    # Lose or Win logic
    if guess not in chosen_word:
        errors += 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if errors == len(stages) - 1:
            game_over = True
            print(f"You lose. The word was {chosen_word}.")

    if "_" not in display:
        game_over = True
        print("You win! You guessed right!")

    # print the ASCII art from 'stages'
    print(stages[errors])
