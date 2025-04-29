# Game mechanics v2 - simulating moving background and adding blocks
# (will be changed to cacti) to show background moving

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

clock = pygame.time.Clock()
quit_game = False

llama_x = 50  # Setting Llama at left of screen
llama_y = 220  # Y-height to be same as ground height
llama_width = 40  # Width of llama block
llama_height = 40  # Height of llama block

# Jumping mechanics
jumping = False
velocity_y = 0
gravity = 1
jump_height = 15
ground_y = 220  # Same as original llama_y
# Background scrolling
scroll_speed = 5
ground_scroll = 0

# Cactus block placeholders
cactus_width = 20
cactus_height = 40
cactus_color = green

# List of cactus positions to test to see if screen is moving
cacti = [{"x": 600, "y": 220}, {"x": 900, "y": 220}, {"x": 1200, "y": 220}]
while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True  # Exits when user presses 'X'
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_SPACE or event.key == pygame.K_UP) and \
                    not jumping:  # Allows jump for both space and up arrow
                jumping = True
                velocity_y -= jump_height
    screen.fill(white)  # Screen/background colour set to white
    # Move the ground line to create moving background effect
    ground_scroll -= scroll_speed
    if abs(ground_scroll) >= 800:
        ground_scroll = 0

    # Draw repeated ground lines to simulate moving background
    for i in range(2):  # Draw two ground lines to cover full width
        pygame.draw.line(screen, black, (ground_scroll + i * 800, 260),
                         (ground_scroll + i * 800 + 800, 260), 2)
    #  Using a sprite (instead of the previous rectangle) to represent llama
    block = pygame.Rect(llama_x, llama_y, llama_width, llama_height)
    llama = pygame.image.load('Llama.png').convert_alpha()
    resized_llama = pygame.transform.smoothscale(llama, [llama_width,
                                                         llama_height])
    screen.blit(resized_llama, block)

    # Gravity + Jump physics
    if jumping:
        llama_y += velocity_y
        velocity_y += gravity

        # Stop jump when llama hits the ground
        if llama_y >= ground_y:
            llama_y = ground_y
            jumping = False
            velocity_y = 0
    # Move and draw cacti blocks
    for cactus in cacti:
        cactus["x"] -= scroll_speed  # Move cactus left
        if cactus["x"] < -cactus_width:  # If off-screen, reset to right
            cactus["x"] = 800 + 200  # Move it further to right (spacing)
        pygame.draw.rect(screen, cactus_color, (cactus["x"], cactus["y"],
                                                cactus_width, cactus_height))
    pygame.display.update()
    clock.tick(60)  # Maximum of 60 fps (frames per second)

pygame.quit()
quit()
