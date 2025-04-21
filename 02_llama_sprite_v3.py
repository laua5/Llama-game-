# Llama sprite v3 - importing Llama sprite to replace block

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
    screen.fill(white)  # Screen/background colour set to white
    pygame.draw.line(screen, black, (0, 260), (800, 260), 2)  # Drawing ground
    #  Using a sprite (instead of the previous rectangle) to represent llama
    block = pygame.Rect(llama_x, llama_y, llama_width, llama_height)
    llama = pygame.image.load('Llama.png').convert_alpha()
    resized_llama = pygame.transform.smoothscale(llama, [llama_width,
                                                         llama_height])
    screen.blit(resized_llama, block)
    pygame.display.update()

pygame.quit()
quit()
