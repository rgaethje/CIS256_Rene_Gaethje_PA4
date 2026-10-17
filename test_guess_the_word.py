# Rene Gaethje
# CIS256 Fall 2026
# Programming Assignment 4 (Testing file)

from guess_the_word import generate_random_word

def test_generate_random_word_from_list():
    """Test whether the selected word comes from the predefined list."""
    word = generate_random_word()
    assert word in GAME_WORD_LIST

def test_generate_random_word_not_in_list():
    """Test whether the selected word IS NOT in predefined list (Negative case)."""
    word = generate_randome_word()
    assert beachfront not in GAME_WORD_LIST
    assert word != "beachfront"

    
