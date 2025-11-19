"""
Demo 6: Flappy Bird Game
=========================
This demo shows:
- Game physics (gravity, jumping)
- Collision detection
- Score tracking
- Game states (playing, game over)
- Random obstacle generation
"""

import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Demo 6: Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 206, 235)
GREEN = (34, 139, 34)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Bird class
class Bird:
    def __init__(self):
        self.x = 80
        self.y = 250
        self.radius = 15
        self.velocity = 0
        self.gravity = 0.5
        self.jump_strength = -5
    
    def jump(self):
        """Make the bird jump"""
        self.velocity = self.jump_strength
    
    def update(self):
        """Update bird position with gravity"""
        self.velocity += self.gravity
        self.y += self.velocity
        
        # Keep bird on screen
        if self.y < self.radius:
            self.y = self.radius
            self.velocity = 0
        if self.y > 600 - self.radius:
            self.y = 600 - self.radius
            self.velocity = 0
    
    def draw(self, surface):
        """Draw the bird"""
        pygame.draw.circle(surface, YELLOW, (int(self.x), int(self.y)), self.radius)
        # Eye
        pygame.draw.circle(surface, BLACK, (int(self.x + 5), int(self.y - 3)), 3)

# Pipe class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.width = 60
        self.gap = 150
        self.top_height = random.randint(100, 400)
        self.speed = 3
        self.passed = False
    
    def update(self):
        """Move pipe to the left"""
        self.x -= self.speed
    
    def draw(self, surface):
        """Draw the pipe"""
        # Top pipe
        pygame.draw.rect(surface, GREEN, (self.x, 0, self.width, self.top_height))
        pygame.draw.rect(surface, BLACK, (self.x, 0, self.width, self.top_height), 2)
        
        # Bottom pipe
        bottom_y = self.top_height + self.gap
        pygame.draw.rect(surface, GREEN, (self.x, bottom_y, self.width, 600 - bottom_y))
        pygame.draw.rect(surface, BLACK, (self.x, bottom_y, self.width, 600 - bottom_y), 2)
    
    def is_offscreen(self):
        """Check if pipe is off screen"""
        return self.x + self.width < 0
    
    def collides_with(self, bird):
        """Check collision with bird"""
        # Check if bird is in pipe's x range
        if bird.x + bird.radius > self.x and bird.x - bird.radius < self.x + self.width:
            # Check if bird hits top or bottom pipe
            if bird.y - bird.radius < self.top_height or bird.y + bird.radius > self.top_height + self.gap:
                return True
        return False

# Game variables
bird = Bird()
pipes = [Pipe(500)]
score = 0
high_score = 0
game_over = False
clock = pygame.time.Clock()
running = True

def reset_game():
    """Reset game to initial state"""
    global bird, pipes, score, game_over
    bird = Bird()
    pipes = [Pipe(500)]
    score = 0
    game_over = False

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_over:
                    bird.jump()
                else:
                    reset_game()
            elif event.key == pygame.K_ESCAPE:
                running = False
    
    if not game_over:
        # Update bird
        bird.update()
        
        # Update pipes
        for pipe in pipes:
            pipe.update()
            
            # Check collision
            if pipe.collides_with(bird):
                game_over = True
                if score > high_score:
                    high_score = score
            
            # Score when passing pipe
            if not pipe.passed and pipe.x + pipe.width < bird.x:
                pipe.passed = True
                score += 1
        
        # Remove offscreen pipes and add new ones
        pipes = [pipe for pipe in pipes if not pipe.is_offscreen()]
        
        if len(pipes) == 0 or pipes[-1].x < 200:
            pipes.append(Pipe(500))
        
        # Check if bird hit ground or ceiling
        if bird.y >= 600 - bird.radius or bird.y <= bird.radius:
            game_over = True
            if score > high_score:
                high_score = score
    
    # Draw everything
    screen.fill(BLUE)
    
    # Draw pipes
    for pipe in pipes:
        pipe.draw(screen)
    
    # Draw bird
    bird.draw(screen)
    
    # Draw score
    font = pygame.font.Font(None, 48)
    score_text = font.render(str(score), True, WHITE)
    score_outline = font.render(str(score), True, BLACK)
    screen.blit(score_outline, (202, 52))
    screen.blit(score_text, (200, 50))
    
    # Draw high score
    small_font = pygame.font.Font(None, 30)
    high_score_text = small_font.render(f"High Score: {high_score}", True, WHITE)
    high_score_outline = small_font.render(f"High Score: {high_score}", True, BLACK)
    screen.blit(high_score_outline, (11, 11))
    screen.blit(high_score_text, (10, 10))
    
    # Draw game over screen
    if game_over:
        # Semi-transparent overlay
        overlay = pygame.Surface((400, 600))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
        
        # Game over text
        game_over_font = pygame.font.Font(None, 72)
        game_over_text = game_over_font.render("GAME OVER", True, RED)
        screen.blit(game_over_text, (50, 200))
        
        # Final score
        final_score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(final_score_text, (120, 280))
        
        # Instructions
        restart_text = small_font.render("Press SPACE to restart", True, WHITE)
        screen.blit(restart_text, (80, 350))
        
        quit_text = small_font.render("Press ESC to quit", True, WHITE)
        screen.blit(quit_text, (100, 380))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
