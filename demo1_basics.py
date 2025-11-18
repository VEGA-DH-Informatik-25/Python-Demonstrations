"""
Demo 1: Basic Pygame - Loops and Conditionals
===============================================
This demo shows:
- while loops (game loop)
- for loops (event handling)
- if/else conditionals (event checking)
- basic pygame setup
"""

import pygame
import sys

# Initialize pygame
pygame.init()

# Create window (800x600 pixels)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Demo 1: Basic Window")

# Colors (RGB tuples)
WHITE = (255, 255, 255)
BLUE = (0, 100, 200)
RED = (200, 0, 0)

# Game loop - runs continuously while True
running = True
color = BLUE

while running:
    # For loop - check all events
    for event in pygame.event.get():
        # If condition - check event type
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Conditional - change color on spacebar
            if event.key == pygame.K_SPACE:
                color = RED if color == BLUE else BLUE

    # Fill screen with current color
    screen.fill(color)
    
    # Draw some shapes
    pygame.draw.circle(screen, WHITE, (400, 300), 50)
    
    # Update display
    pygame.display.flip()

pygame.quit()
sys.exit()
