"""
Demo 4: Lists and Iteration
============================
This demo shows:
- Lists (collections of items)
- Adding items to lists (.append)
- Iterating through lists (for loop)
- List indexing and length
"""

import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Demo 4: Lists")

# List of circles - each circle is a dictionary
circles = []

# Function to create a circle
def create_circle():
    """Create a circle with random position and color"""
    circle = {
        'x': random.randint(50, 750),
        'y': random.randint(50, 550),
        'color': (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
        'radius': random.randint(20, 50)
    }
    return circle

# Add 5 circles to start
for i in range(5):
    circles.append(create_circle())

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Add a new circle to the list
            circles.append(create_circle())

    screen.fill((240, 240, 240))
    
    # Iterate through list and draw each circle
    for circle in circles:
        pygame.draw.circle(screen, circle['color'], 
                          (circle['x'], circle['y']), circle['radius'])
    
    # Display list information
    font = pygame.font.Font(None, 30)
    text = font.render(f"Circles: {len(circles)} (Click to add more)", True, (0, 0, 0))
    screen.blit(text, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
