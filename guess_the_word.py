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

def generate_random_word():
    """Generate random word from a predefined list (GAME_WORD_LIST)"""
    idx = random.randint(0, len(GAME_WORD_LIST))
    word = GAME_WORD_LIST[idx]
    return word

def prepare_word(word):
    """Set up placeholder view for puzzle word"""
    word_incomplete = []
    for letter in word:
        word_incomplete.append(" _ ")
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
    with all instances of the guessed letter that are found in puzzle word;
    display results or keep guessing message; allow user to keep guessing
    until puzzle solved or they run out of guesses.
    """
    
                  
    


def main():
    """Main program logic"""
    word = generate_random_word()
    print(word)
    word_incomplete = prepare_word(word)
    print(word_incomplete)
    guess = get_guess()
    print(guess)
    
    


if __name__ == "__main__":
    main()

