"""
Demo 2: Variables and Data Types
=================================
This demo shows:
- Variables (numbers, strings, booleans)
- Different data types (int, float, tuple)
- Mathematical operations
- Moving objects with variables
"""

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Demo 2: Variables & Movement")

# Variables with different data types
x = 50              # Integer
y = 300.0           # Float
speed = 2           # Integer
direction = 1       # Integer (1 or -1)
color = (255, 0, 0) # Tuple (RGB)
radius = 30         # Integer

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mathematical operations - update position
    x = x + (speed * direction)
    
    # Conditional - reverse direction at edges
    if x > 800 - radius or x < radius:
        direction = direction * -1  # Multiply to reverse

    # Fill and draw
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, color, (int(x), int(y)), radius)
    
    # Display variable values as text
    font = pygame.font.Font(None, 36)
    text = font.render(f"X: {int(x)} Speed: {speed}", True, (0, 0, 0))
    screen.blit(text, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
sys.exit()
