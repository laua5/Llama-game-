# Game display v3 - creating global variables for colour and font

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 300))  # Screen dimensions (W * H)
game_icon = pygame.image.load('llama_icon.png')
pygame.display.set_icon(game_icon)  # Setting game icon
pygame.display.set_caption("Llama game - By Alex Lau")  # Adding title

# Tuples containing the colours to be used in game
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (188, 227, 199)

# Fonts for the game
score_font = pygame.font.SysFont("arialblack", 20)
exit_font = pygame.font.Font("freesansbold.ttf", 30)

pygame.quit()
quit()
