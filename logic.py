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
        self.string_scoreboard = " ".join(self.scoreboard)

        # Sets the scoreboard
        for letter in self.hangman_word:
            self.correct_letters += letter
            self.scoreboard += "_"

        if self.lives_left > 0:
            self.response = self.string_scoreboard + "            You have already selected: " + self.selected_letters
            if self.scoreboard.__contains__(self.guess):
                self.response = "Please enter a unique value: "
            else:
                self.selected_letters += self.guess + " "
                for index, values in enumerate(self.correct_letters):
                    if values == guess:
                        self.scoreboard[index - 1] = self.guess

                if not self.correct_letters.__contains__(self.guess) and self.lives_left != 6:
                    self.response = "WRONG!!! You only have \n" + str(self.lives_left) + " lives left!"
                elif not self.scoreboard.__contains__("_"):
                    self.response = "Congratulations! You won the game!"
            if self.lives_left == 0:
                self.response = "Game over! Better luck next time! The word was: " + self.hangman_word
