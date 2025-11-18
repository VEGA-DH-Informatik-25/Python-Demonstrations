"""
Demo 3: Functions
=================
This demo shows:
- Function definition with def
- Function parameters and return values
- Reusable code
- Event handling with functions
"""

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Demo 3: Functions")

# Function definition - takes parameters, returns value
def get_random_color():
    """Returns a random RGB color tuple"""
    import random
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def draw_circle(surface, color, x, y, radius):
    """Function to draw a circle - reusable code"""
    pygame.draw.circle(surface, color, (x, y), radius)

def draw_square(surface, color, x, y, size):
    """Function to draw a square"""
    pygame.draw.rect(surface, color, (x - size//2, y - size//2, size, size))

# Variables
circle_color = (255, 0, 0)
square_color = (0, 0, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Call function - changes colors randomly
            circle_color = get_random_color()
            square_color = get_random_color()

    screen.fill((255, 255, 255))
    
    # Call functions to draw shapes
    draw_circle(screen, circle_color, 300, 300, 80)
    draw_square(screen, square_color, 500, 300, 100)
    
    # Instructions
    font = pygame.font.Font(None, 30)
    text = font.render("Click to change colors!", True, (0, 0, 0))
    screen.blit(text, (250, 50))
    
    pygame.display.flip()

pygame.quit()
sys.exit()
