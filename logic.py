"""
This is a cool command line hangman game to flex my skills!
"""

# Imports the 2 different functions needed to run the game
from words import words
from random import randint


class Logic:
    def __init__(self, guess):
        self.guess = guess
        self.hangman_word = words[randint(1, 200)]
        self.lives_left = 7
        self.scoreboard = []
        self.correct_letters = []
        self.selected_letters = ""
        self.response = ""

        # Sets the scoreboard
        for letter in self.hangman_word:
            self.correct_letters += letter
            self.scoreboard += "_"

