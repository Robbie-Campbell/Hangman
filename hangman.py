"""
This is a cool command line hangman game to flex my skills!
"""

from words import words
from random import randint

hangman_word = words[randint(1, 200)]
lives_left = 10
scoreboard = []
correct_letters = []
selected_letters = ""

for letter in hangman_word:
    correct_letters += letter
    scoreboard += "_"
print(correct_letters)


while lives_left > 0:
    string_scoreboard = " ".join(scoreboard)
    print(string_scoreboard + "            You have already selected: " + selected_letters)
    guess = input("Please enter a letter: ")
    index = -1
    if scoreboard.__contains__(guess):
        print("Please enter a unique value: ")
        continue
    else:
        for values in correct_letters:
            index += 1
            if values == guess:
                correct = scoreboard[index] = guess
                selected_letters += guess + " "
        if not correct_letters.__contains__(guess):
            lives_left -= 1
            print("Wrong!!!")
            print("You only have " + str(lives_left) + " lives left!")
    if lives_left == 0:
        print("Game over! Better luck next time! The word was: " + hangman_word)
    elif scoreboard == hangman_word:
        print("Congratulations! You won the game!")
