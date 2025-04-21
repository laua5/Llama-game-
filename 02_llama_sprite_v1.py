# Llama sprite v1 - adding block as placeholder to correct coordinates

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

quit_game = False

llama_x = 50  # Setting Llama at left of screen
llama_y = 220  # Y-height to be same as ground height
llama_width = 20  # Width of llama block
llama_height = 40  # Height of llama block

while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True  # Exits when user presses 'X'
    # Create rectangle for llama
    pygame.draw.rect(screen, red, [llama_x, llama_y, llama_width,
                                   llama_height])
    pygame.display.update()

pygame.quit()
quit()
