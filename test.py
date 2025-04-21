import pygame

pygame.init()

screen = pygame.display.set_mode((800, 300))
game_icon = pygame.image.load('llama_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Llama game - By Alex Lau")

# Colours
black = (0, 0, 0)
white = (255, 255, 255)

# Fonts
score_font = pygame.font.SysFont("arialblack", 20)
exit_font = pygame.font.Font("freesansbold.ttf", 30)

clock = pygame.time.Clock()
quit_game = False

# Llama position and size
llama_x = 50
llama_y = 220  # This is the top of the llama
llama_width = 20
llama_height = 40

# Jumping mechanics
is_jumping = False
velocity_y = 0
gravity = 1
jump_strength = 15
ground_y = 220  # Same as original llama_y

# Load llama image once outside the loop
llama = pygame.image.load('Llama.png').convert_alpha()
llama = pygame.transform.smoothscale(llama, [llama_width, llama_height])

while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not is_jumping:
        is_jumping = True
        velocity_y = -jump_strength

    # Gravity + Jump physics
    if is_jumping:
        llama_y += velocity_y
        velocity_y += gravity

        # Stop jump when llama hits the ground
        if llama_y >= ground_y:
            llama_y = ground_y
            is_jumping = False
            velocity_y = 0

    # Draw everything
    screen.fill(white)
    pygame.draw.line(screen, black, (0, 260), (800, 260), 2)  # Ground
    screen.blit(llama, (llama_x, llama_y))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
