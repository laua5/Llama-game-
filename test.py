# Cactus sprite v3 - Creating random locations for cacti

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
jump_height = 12
ground_y = 220  # Same as original llama_y

# Background scrolling
scroll_speed = 5
ground_scroll = 0

# Cactus block placeholders
cactus_width = 40
cactus_height = 40
cactus_img = pygame.image.load('cactus.png').convert_alpha()
cactus_img = pygame.transform.smoothscale(cactus_img, (cactus_width,
                                                       cactus_height))
cacti = []
spawn_delay = 90  # frames
spawn_timer = 0


# Main game loop as a function
def game_loop():
    global llama_y, jumping, velocity_y, ground_scroll, cacti, spawn_timer

    llama_y = 220
    jumping = False
    velocity_y = 0
    ground_scroll = 0
    cacti = []
    spawn_timer = 0

    quit_game = False
    while not quit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE or event.key == pygame.K_UP) and not jumping:
                    jumping = True
                    velocity_y -= jump_height

        screen.fill(white)
        ground_scroll -= scroll_speed
        if abs(ground_scroll) >= 800:
            ground_scroll = 0

        for i in range(2):
            pygame.draw.line(screen, black, (ground_scroll + i * 800, 260),
                             (ground_scroll + i * 800 + 800, 260), 2)

        block = pygame.Rect(llama_x, llama_y, llama_width, llama_height)
        llama = pygame.image.load('Llama.png').convert_alpha()
        resized_llama = pygame.transform.smoothscale(llama, [llama_width, llama_height])
        screen.blit(resized_llama, block)

        if jumping:
            llama_y += velocity_y
            velocity_y += gravity
            if llama_y >= ground_y:
                llama_y = ground_y
                jumping = False
                velocity_y = 0

        llama_hitbox = pygame.Rect(llama_x + 3, llama_y + 5, llama_width - 6, llama_height - 10)
        pygame.draw.rect(screen, red, llama_hitbox, 2)

        min_cactus_gap = 150
        spawn_timer += 1
        if spawn_timer > spawn_delay:
            if not cacti or cacti[-1]["x"] < (800 - min_cactus_gap):
                cactus_x = 800 + random.randint(0, 100)
                cacti.append({"x": cactus_x, "y": 220})
                spawn_timer = 0

        for cactus in cacti[:]:
            cactus["x"] -= scroll_speed
            cactus_rect = pygame.Rect(cactus["x"], cactus["y"], cactus_width, cactus_height)
            screen.blit(cactus_img, (cactus["x"], cactus["y"]))
            pygame.draw.rect(screen, black, cactus_rect, 2)

            if llama_hitbox.colliderect(cactus_rect):
                print("Game Over")
                return  # Exit game_loop and allow restart later

            if cactus["x"] < -cactus_width:
                cacti.remove(cactus)

        pygame.display.update()
        clock.tick(60)

# === Main Game Loop Controller ===
while True:
    game_loop()
    # You can add a restart screen here later
    # For now, it immediately restarts the game
