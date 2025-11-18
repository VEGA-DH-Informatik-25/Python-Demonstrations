"""
Demo 5: Classes and Object-Oriented Programming
================================================
This demo shows:
- Class definition (blueprint for objects)
- __init__ method (constructor)
- Instance variables (self.x, self.y)
- Methods (functions inside classes)
- Creating multiple objects from a class
"""

import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Demo 5: Classes & OOP")

# Class definition - blueprint for Ball objects
class Ball:
    """A bouncing ball object"""
    
    def __init__(self, x, y):
        """Constructor - runs when creating a new Ball"""
        self.x = x
        self.y = y
        self.radius = random.randint(15, 40)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.speed_x = random.choice([-3, -2, 2, 3])
        self.speed_y = random.choice([-3, -2, 2, 3])
    
    def move(self):
        """Method to move the ball"""
        self.x += self.speed_x
        self.y += self.speed_y
        
        # Bounce off edges
        if self.x < self.radius or self.x > 800 - self.radius:
            self.speed_x *= -1
        if self.y < self.radius or self.y > 600 - self.radius:
            self.speed_y *= -1
    
    def draw(self, surface):
        """Method to draw the ball"""
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

# Create list of Ball objects
balls = []
for i in range(5):
    balls.append(Ball(random.randint(100, 700), random.randint(100, 500)))

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Create new Ball object at mouse position
            balls.append(Ball(event.pos[0], event.pos[1]))

    screen.fill((255, 255, 255))
    
    # Call methods on each Ball object
    for ball in balls:
        ball.move()    # Call move method
        ball.draw(screen)  # Call draw method
    
    # Display info
    font = pygame.font.Font(None, 30)
    text = font.render(f"Balls: {len(balls)} (Click to add)", True, (0, 0, 0))
    screen.blit(text, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
