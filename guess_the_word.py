# Rene Gaethje
# CIS256 Fall 2026
# Programming Assignment 4

import random


# Define constants
GAME_WORD_LIST = [
    "oceanfront", "lakehouse", "river", "alligator", "dinosaur", "sailboat",
    "heartstrings", "hippopotamus", "lovestruck", "rollerskating",
    "lighthouse", "coastline", "waterfall", "shipwreck",
    "driftwood", "coralreef", "sunshine", "daydream",
    "sweetheart", "butterflies", "breathtaking", "parasailing",
    "thunderstorm", "rollercoaster", "dragonfly", "moonlight"
]

STRIKES = [
    # 0 incorrect guesses
    r""" ____  ____  ____  ____  ____  ____ 
|    ||    ||    ||    ||    ||    |
|    ||    ||    ||    ||    ||    |
|    ||    ||    ||    ||    ||    |
|____||____||____||____||____||____|
    """,
    
    # 1 incorrect guess
    r""" ____  ____  ____  ____  ____  ____ 
|\  /||    ||    ||    ||    ||    |
| \/ ||    ||    ||    ||    ||    |
| /\ ||    ||    ||    ||    ||    |
|/__\||____||____||____||____||____|
    """,
    
    # 2 incorrect guesses
    r""" ____  ____  ____  ____  ____  ____ 
|\  /||\  /||    ||    ||    ||    |
| \/ || \/ ||    ||    ||    ||    |
| /\ || /\ ||    ||    ||    ||    |
|/__\||/__\||____||____||____||____|
    """,
    
    # 3 incorrect guesses
    r""" ____  ____  ____  ____  ____  ____ 
|\  /||\  /||\  /||    ||    ||    |
| \/ || \/ || \/ ||    ||    ||    |
| /\ || /\ || /\ ||    ||    ||    |
|/__\||/__\||/__\||____||____||____|
    """,
    
    # 4 incorrect guesses
    r""" ____  ____  ____  ____  ____  ____ 
|\  /||\  /||\  /||\  /||    ||    |
| \/ || \/ || \/ || \/ ||    ||    |
| /\ || /\ || /\ || /\ ||    ||    |
|/__\||/__\||/__\||/__\||____||____|
    """,

    # 5 incorrect guesses
    r""" ____  ____  ____  ____  ____  ____ 
|\  /||\  /||\  /||\  /||\  /||    |
| \/ || \/ || \/ || \/ || \/ ||    |
| /\ || /\ || /\ || /\ || /\ ||    |
|/__\||/__\||/__\||/__\||/__\||____|
    """,

    # 6 incorrect guesses
    r""" ____  ____  ____  ____  ____  ____ 
|\  /||\  /||\  /||\  /||\  /||\  /|
| \/ || \/ || \/ || \/ || \/ || \/ |
| /\ || /\ || /\ || /\ || /\ || /\ |
|/__\||/__\||/__\||/__\||/__\||/__\|
    """
]

def generate_random_word():
    """Generate random word from a predefined list (GAME_WORD_LIST)"""
    idx = random.randint(0, len(GAME_WORD_LIST) - 1)
    word = GAME_WORD_LIST[idx]
    return word

def prepare_word(word):
    """Set up placeholder view for puzzle word"""
    word_incomplete = []
    for letter in word:
        word_incomplete.append("_")
    return word_incomplete

def get_guess():
    """Get guess from user; validate input is alpha; force lowercase"""
    while True:
        guess = input("\nPick a letter.").strip().lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid input. Please enter a single letter form A - Z.")

def check_guess(word, word_incomplete):
    """
    Check to see if guess is in the puzzle word; update word_incomplete
    with all instances of the guessed letter that are found in word;
    allow user to keep guessing letters until the puzzle is solved or
    until they reach max_incorrect guess count.
    """

    incorrect_letters = []  # store previously guesses letters
    incorrect_count = 0  # keep track of how many incorrect guesses
    max_incorrect = 6

    # Keep asking for user guesses while game is in process
    while "_" in word_incomplete and incorrect_count < max_incorrect:
        # Format game screen
        print("    *************************")
        print("       GUESS THE WORD GAME   ")
        print("    *************************")
        print(STRIKES[incorrect_count])
        print("Puzzle: ", *word_incomplete)
        print("Guessed letters: ", *incorrect_letters)

        # Get user guess
        guess = get_guess()
        if guess in incorrect_letters:
            print(f"You already guessed '{guess}'. Try a different letter!")
            # Leave loop; ask user for new letter; do not count as incorrect guess
            continue 

        # Check if guess is NOT in the word puzzle
        if guess not in word:
            incorrect_letters.append(guess)
            incorrect_count +=1
            print("Letter is not in puzzle. Please try again.\n") 
        else:
            print("Good guess!\n")
            # If guess is in word, update all matching instances
            for idx, letter in enumerate(word):
                if guess.lower() == letter.lower():
                    word_incomplete[idx] = guess

    # Display game title and status with filled word at end of game.
    print("    *************************")
    print("       GUESS THE WORD GAME   ")
    print("    *************************")
    print(STRIKES[incorrect_count])
    print("Puzzle: ", *word_incomplete)
    print("Guessed letters: ", *incorrect_letters)

    # Display win or lose message
    if "_" not in word_incomplete:
        print(f"\nCongratulations! You solved the puzzle!\n "
              f"The word is {word}\n")
    else:
        print(f"\nToo many incorrect guesses! You lose! :-(\nThe word is {word}\n")              
    

def main():
    """Main program logic"""
    word = generate_random_word()
    word_incomplete = prepare_word(word)
    check_guess(word, word_incomplete)
  


if __name__ == "__main__":
    main()

