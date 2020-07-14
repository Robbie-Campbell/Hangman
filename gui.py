import pygame
from pygame.locals import *
from logic import Logic
from textbox import InputBox

pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

bg = pygame.image.load("Images/bg.png")

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")
surface = pygame.Surface((50, 50))


class Hangman(object):

    hangman_images = [pygame.image.load("Images/Hangman_stages/H%s.png" % frames) for frames in range(1, 8)]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.images = self.hangman_images
        self.current = 0


def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele + " "

        # return string
    return str1


hangman = Hangman(700, 150)
clock = pygame.time.Clock()
textinput = InputBox(100, 100, 140, 32)
letter = ''
game_loop = Logic(letter)


def main():
    global letter
    running = True
    input_box = InputBox(100, 100, 140, 32)
    print(game_loop.hangman_word)
    win_condition = "You have " + str(game_loop.lives_left) + " lives left."
    while running:
        window.blit(bg, (0, 0))
        font = pygame.font.SysFont("comicsans", 45)
        window.blit(hangman.hangman_images[hangman.current], (hangman.x, hangman.y))
        for event in pygame.event.get():
            input_box.handle_event(event)
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_RETURN:
                    deduction = 0
                    for index, values in enumerate(game_loop.correct_letters):
                        win_condition = "You have " + str(game_loop.lives_left) + " lives left."
                        if not game_loop.scoreboard.__contains__("_"):
                            win_condition = "Congratulations, you won the game!"
                        if input_box.guess.__contains__(values):
                            game_loop.scoreboard[index] = values + " "
                            deduction += 1
                        elif game_loop.lives_left == 0:
                            win_condition = "You Lose! the word was: " + game_loop.hangman_word
                        if len(game_loop.scoreboard) == len(game_loop.correct_letters) - deduction:
                            print((len(game_loop.correct_letters) - deduction))
                            game_loop.lives_left -= 1
                            hangman.current += 1

        input_box.update()
        input_box.draw(window)
        text = font.render(win_condition, True, (255, 255, 255))
        letters = font.render(listToString(game_loop.scoreboard), True, (255, 255, 255))
        window.blit(letters, (100, 300))
        window.blit(text, (100, 500))
        pygame.display.update()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
