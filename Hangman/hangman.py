"""
@author : nishant sanjay kumbhar
@goal  : to create the hangman game in python
"""
import sys
import random
import string

from words import words


def get_valid_word(words: list) -> str:
    """
    this function used to get valid word from words list because some words are separated by using spaces and dashes(-).
    so we looping through list until we get a valid word i.e without spaces and dashes(-)
    :param words: list of words : list
    :return: return a valid word from list of words
    """
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    print(word)
    word_letters = set(word)  # set actually separate the letters from word but it doesn't include double or more than letters
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:
        print("You have used these letters : ", " ".join(used_letters))
        """
        ' '.join(['a', 'b', 'cd']) what it does is -> a b cd -> join the list with string given at the first i.e ' ' in between elements.
        """
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(word_list)
        print("Current Word : ", " ".join(word_list))
        user_letter = input("Enter the Letter : ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print("You have already used that letter, Please try Again")
        else:
            print("Invalid letter !, Please try Again")


hangman()
