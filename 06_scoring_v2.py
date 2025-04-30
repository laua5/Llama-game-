# Scoring v2 - keeping track of high score

import pygame
import random


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
msg_font = pygame.font.SysFont("arialblack,", 20)

clock = pygame.time.Clock()

# Cactus block placeholders
cactus_width = 40
cactus_height = 40
cactus_img = pygame.image.load('cactus.png').convert_alpha()
cactus_img = pygame.transform.smoothscale(cactus_img, (cactus_width,
                                                       cactus_height))


# Function to keep track of highest score - writes value to a file (from snake
# game)
def load_highest_score():
    try:
        hi_score_file = open("Hi_score.text", 'r')
    except IOError:
        hi_score_file = open("Hi_score.text", 'w')
        hi_score_file.write("0")
    hi_score_file = open("HI_score.text", 'r')
    value = hi_score_file.read()
    hi_score_file.close()
    return value


# Display player score throughout the game (from snake game)
def player_score(score, score_colour):
    display_score = score_font.render(f"Score: {score}", True, score_colour)
    screen.blit(display_score, (680, 20))  # Coordinates for top right


# To put messages on the screen (from snake game)
def message(msg, txt_colour, bkgd_colour):
    txt = msg_font.render(msg, True, txt_colour, bkgd_colour)

    # Centre rectangle: 800/2 = 400 and 300/2 = 15
    text_box = txt.get_rect(center=(400, 150))
    screen.blit(txt, text_box)


def game_loop():
    quit_game = False
    game_over = False
    # Jumping Mechanics
    jumping = False
    velocity_y = 0
    gravity = 1
    jump_height = 18
    ground_y = 220  # Same as original llama_y

    llama_x = 50  # Setting Llama at left of screen
    llama_y = 220  # Y-height to be same as ground height
    llama_width = 40  # Width of llama block
    llama_height = 40  # Height of llama block

    # Background scrolling
    scroll_speed = 5
    ground_scroll = 0

    cacti = []
    spawn_delay = 90  # frames
    spawn_timer = 0
    start_time = pygame.time.get_ticks()  # Start counting time
    # Load the high score
    high_score = load_highest_score()
    print(f"high_score test: {high_score}")  # For testing purposes only
    while not quit_game:
        # Give user the option to quit or play again when they die
        while game_over:
            screen.fill(white)
            message("You died! Press 'Q' to play Quit or 'A' to play again",
                    black, white)
            pygame.display.update()

            # Check if user wants to quit (Q) or play again (A)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit_game = True
                        game_over = False
                    if event.key == pygame.K_a:
                        game_loop()  # Restart the main game loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True  # Exits when user presses 'X'
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE or event.key == pygame.K_UP) \
                        and not jumping:  # Allows jump for both space and up
                    # arrow
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
        #  Using a sprite (instead of the previous square) to represent llama
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
        # Create a rect for the llama each frame
        llama_hitbox = pygame.Rect(llama_x + 3, llama_y + 5,
                                   llama_width - 6, llama_height - 10)
        # Adjusting for hitbox issues
        pygame.draw.rect(screen, red, llama_hitbox, 2)  # For hitbox testing

        min_cactus_gap = 150  # minimum pixels between cacti
        spawn_timer += 1
        if spawn_timer > spawn_delay:
            if not cacti or cacti[-1]["x"] < (800 - min_cactus_gap):
                cactus_x = 800 + random.randint(0, 100)
                cacti.append({"x": cactus_x, "y": 220})
                spawn_timer = 0
        # Calculate score as seconds passed since start of game
        current_time = pygame.time.get_ticks()
        score = (current_time - start_time) // 1000  # Convert ms to seconds
        player_score(score, black)  # Show score on screen

        # Move and draw cacti blocks
        for cactus in cacti[:]:
            cactus["x"] -= scroll_speed  # move left
            cactus_rect = pygame.Rect(cactus["x"], cactus["y"], cactus_width,
                                      cactus_height)
            screen.blit(cactus_img, (cactus["x"], cactus["y"]))
            pygame.draw.rect(screen, black, cactus_rect, 2)  # Hitbox testing

            # Collision detection
            if llama_hitbox.colliderect(cactus_rect):
                game_over = True

            # Remove cactus if it moves off-screen
            if cactus["x"] < -cactus_width:
                cacti.remove(cactus)

        pygame.display.update()
        clock.tick(60)  # Maximum of 60 fps (frames per second)

    pygame.quit()
    quit()


# Main loop
game_loop()
