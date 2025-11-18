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
    
    def check_collision(self, other):
        """Check if this ball collides with another ball"""
        # Calculate distance between centers
        dx = self.x - other.x
        dy = self.y - other.y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        
        # Check if balls are overlapping
        return distance < self.radius + other.radius
    
    def handle_collision(self, other):
        """Handle collision physics with another ball"""
        # Calculate angle between balls
        dx = other.x - self.x
        dy = other.y - self.y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        
        if distance == 0:
            return
        
        # Normalize direction
        dx /= distance
        dy /= distance
        
        # Calculate relative velocity
        dvx = self.speed_x - other.speed_x
        dvy = self.speed_y - other.speed_y
        
        # Calculate dot product
        dot_product = dvx * dx + dvy * dy
        
        # Only collide if balls are moving towards each other
        if dot_product > 0:
            # Simple elastic collision - exchange velocities along collision axis
            self.speed_x -= dot_product * dx
            self.speed_y -= dot_product * dy
            other.speed_x += dot_product * dx
            other.speed_y += dot_product * dy
            
            # Separate balls to prevent overlap
            overlap = self.radius + other.radius - distance
            self.x -= overlap * dx * 0.5
            self.y -= overlap * dy * 0.5
            other.x += overlap * dx * 0.5
            other.y += overlap * dy * 0.5

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
    
    # Check for collisions between all pairs of balls
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            if balls[i].check_collision(balls[j]):
                balls[i].handle_collision(balls[j])
    
    # Draw all balls
    for ball in balls:
        ball.draw(screen)  # Call draw method
    
    # Display info
    font = pygame.font.Font(None, 30)
    text = font.render(f"Balls: {len(balls)} (Click to add)", True, (0, 0, 0))
    screen.blit(text, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
