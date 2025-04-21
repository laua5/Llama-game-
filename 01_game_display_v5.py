import pygame

# Initialize pygame
pygame.init()

# ===== GUI Dimensions =====
WIDTH = 800
HEIGHT = 300

# ===== Display Setup =====
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Game by YourName")

# Set Game Icon (Replace with your own icon path)
try:
    ICON = pygame.image.load("assets/icon.png")
    pygame.display.set_icon(ICON)
except:
    print("Icon not found, using default.")

# ===== Colors =====
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (100, 100, 100)
RED = (255, 0, 0)

# ===== Font =====
FONT = pygame.font.SysFont(None, 36)
