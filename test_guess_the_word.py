# Rene Gaethje
# CIS256 Fall 2026
# Programming Assignment 4 (Testing file)

from guess_the_word import generate_random_word, GAME_WORD_LIST, prepare_word, check_guess

def test_generate_random_word_from_list():
    """Test whether the selected word comes from the predefined list."""
    word = generate_random_word()
    assert word in GAME_WORD_LIST

def test_prepare_word():
    """Test that prepare_word creates the correct number of underscores."""
    word = "dog"
    word_incomplete = prepare_word(word)
    assert word_incomplete == ['_', '_', '_']

def test_check_guess(monkeypatch):
    """Test correct guesses will solve puzzle successfully."""
    word = "cat"
    word_incomplete = ['_', '_', '_']

    # Simulate user input
    inputs = iter(['d','e','c','c','a','t'])

    # use hardcoded values to simulate user input 
    monkeypatch.setattr('guess_the_word.get_guess', lambda: next(inputs))

    # Run function
    check_guess(word, word_incomplete)

    # Assert that the puzzle is now solved
    assert "_" not in word_incomplete
    
