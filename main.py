import pygame
import os
import math
import random

# Setup Display
pygame.init()
WIDTH, HEIGHT = 800,500
win_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HangMan Game (-_-)")

# Button Variables
RADIUS = 20
GAP = 15
letters = []
StartX = round((WIDTH - (RADIUS * 2 + GAP) * 13 ) / 2)
StartY = 400
A = 65
for i in range (26):
    x = StartX + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = StartY + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# Fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 65)
TITLE_FONT = pygame.font.SysFont('comicsans', 75)

# Game Images
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# Game Variable
hangman_stat = 0
words = ["PYTHON", "NISARGSIR", "NOSUICIDE", "DEVZARRY"]
word = random.choice(words)
guessed = []

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)



def draw():
    win_screen.fill(WHITE)
    # Draw Title
    text = TITLE_FONT.render("ZARRY's HANGMAN", 1, BLACK, RED)
    win_screen.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # Draw Word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win_screen.blit(text, (400,200))
    
    # Draw Button
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win_screen, BLACK, (x,y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, RED)
            win_screen.blit(text, (x - text.get_width()/2 , y- text.get_height()/2))

    win_screen.blit(images[hangman_stat], (50, 100))
    pygame.display.update()

# MESSAGE SETUP
def display_message(message):
    pygame.time.delay(1000)
    win_screen.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win_screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(2000)


def main():
    global hangman_stat

    # Setup Game_Loop
    FPS = 60
    time_track = pygame.time.Clock()
    run = True

    #Game logic
    while run:
        time_track.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # quit
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()  # X-Y Position of mouse
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        distance = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if distance < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_stat += 1
        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            display_message("YOU WON!")
            break

        if hangman_stat == 6:
            display_message("YOU LOST!")
            break

while True:
    main()
    break
pygame.quit()