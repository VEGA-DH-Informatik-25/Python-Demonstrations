"""
Tic Tac Toe with Pygame
========================
Features:
- Graphical pygame interface
- Player vs Player mode
- Player vs Computer (Easy - Random)
- Player vs Computer (Hard - Minimax AI)
- Click to place marks
- Visual feedback and game state display
"""

import math
import random
import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WINDOW_SIZE = 600
GRID_SIZE = 3
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
LINE_WIDTH = 15
MARK_WIDTH = 15

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 100, 200)
RED = (200, 50, 50)
GREEN = (50, 200, 50)
LIGHT_BLUE = (173, 216, 230)

# Create window
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + 100))
pygame.display.set_caption("Tic Tac Toe")


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
    
    def available_moves(self):
        """Return list of available positions"""
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        """Check if there are empty squares"""
        return ' ' in self.board
    
    def num_empty_squares(self):
        """Count empty squares"""
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        """Make a move if valid"""
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        """Check if the last move resulted in a win"""
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        
        return False
    
    def reset(self):
        """Reset the board"""
        self.board = [' ' for _ in range(9)]
        self.current_winner = None


class ComputerPlayer:
    def __init__(self, letter):
        self.letter = letter
    
    def get_move(self, game):
        """Get random move from computer"""
        return random.choice(game.available_moves())


class MinimaxPlayer:
    def __init__(self, letter):
        self.letter = letter
    
    def get_move(self, game):
        """Get best move using minimax algorithm"""
        if len(game.available_moves()) == 9:
            # First move, choose random corner or center
            return random.choice([0, 2, 4, 6, 8])
        else:
            # Use minimax algorithm
            return self.minimax(game, self.letter)['position']
    
    def minimax(self, state, player):
        """Minimax algorithm implementation"""
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'
        
        # Check if previous move was a winner
        if state.current_winner == other_player:
            return {
                'position': None,
                'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)
            }
        elif not state.empty_squares():
            return {'position': None, 'score': 0}
        
        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}
        
        for possible_move in state.available_moves():
            # Try the move
            state.make_move(possible_move, player)
            # Simulate game after making that move
            sim_score = self.minimax(state, other_player)
            
            # Undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
            
            # Update best move
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        
        return best


def draw_grid():
    """Draw the tic tac toe grid"""
    screen.fill(WHITE)
    
    # Draw vertical lines
    for i in range(1, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_SIZE), LINE_WIDTH)
    
    # Draw horizontal lines
    for i in range(1, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WINDOW_SIZE, i * CELL_SIZE), LINE_WIDTH)


def draw_marks(game):
    """Draw X's and O's on the board"""
    for i, mark in enumerate(game.board):
        if mark != ' ':
            row = i // 3
            col = i % 3
            center_x = col * CELL_SIZE + CELL_SIZE // 2
            center_y = row * CELL_SIZE + CELL_SIZE // 2
            
            if mark == 'X':
                # Draw X
                offset = CELL_SIZE // 3
                pygame.draw.line(screen, BLUE, 
                               (center_x - offset, center_y - offset),
                               (center_x + offset, center_y + offset), MARK_WIDTH)
                pygame.draw.line(screen, BLUE,
                               (center_x + offset, center_y - offset),
                               (center_x - offset, center_y + offset), MARK_WIDTH)
            else:  # O
                # Draw O
                radius = CELL_SIZE // 3
                pygame.draw.circle(screen, RED, (center_x, center_y), radius, MARK_WIDTH)


def draw_status(text, color=BLACK):
    """Draw status text at the bottom"""
    pygame.draw.rect(screen, LIGHT_BLUE, (0, WINDOW_SIZE, WINDOW_SIZE, 100))
    font = pygame.font.Font(None, 48)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE + 50))
    screen.blit(text_surface, text_rect)


def draw_button(text, rect, color):
    """Draw a button"""
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BLACK, rect, 3)
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)


def show_menu():
    """Show game mode selection menu"""
    menu_running = True
    
    # Button rectangles
    button_width = 400
    button_height = 60
    button_x = (WINDOW_SIZE - button_width) // 2
    
    pvp_button = pygame.Rect(button_x, 150, button_width, button_height)
    easy_button = pygame.Rect(button_x, 250, button_width, button_height)
    hard_button = pygame.Rect(button_x, 350, button_width, button_height)
    quit_button = pygame.Rect(button_x, 450, button_width, button_height)
    
    while menu_running:
        screen.fill(WHITE)
        
        # Title
        title_font = pygame.font.Font(None, 72)
        title = title_font.render("TIC TAC TOE", True, BLACK)
        screen.blit(title, (WINDOW_SIZE // 2 - title.get_width() // 2, 50))
        
        # Draw buttons
        draw_button("Player vs Player", pvp_button, GREEN)
        draw_button("vs Computer (Easy)", easy_button, BLUE)
        draw_button("vs Computer (Hard)", hard_button, RED)
        draw_button("Quit", quit_button, GRAY)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pvp_button.collidepoint(event.pos):
                    return "pvp"
                elif easy_button.collidepoint(event.pos):
                    return "easy"
                elif hard_button.collidepoint(event.pos):
                    return "hard"
                elif quit_button.collidepoint(event.pos):
                    return None
    
    return None


def get_cell_from_mouse(pos):
    """Convert mouse position to cell index"""
    x, y = pos
    if y >= WINDOW_SIZE:  # Clicked in status area
        return None
    col = x // CELL_SIZE
    row = y // CELL_SIZE
    return row * 3 + col


def play_game(game_mode):
    """Main game loop"""
    game = TicTacToe()
    current_player = 'X'
    
    # Set up players
    if game_mode == "pvp":
        o_player = None
        status_text = "Player X's Turn"
    elif game_mode == "easy":
        o_player = ComputerPlayer('O')
        status_text = "Your Turn (X)"
    else:  # hard
        o_player = MinimaxPlayer('O')
        status_text = "Your Turn (X)"
    
    game_over = False
    clock = pygame.time.Clock()
    
    running = True
    while running:
        # Draw board
        draw_grid()
        draw_marks(game)
        
        if game_over:
            if game.current_winner:
                winner_text = f"{game.current_winner} Wins!"
                color = BLUE if game.current_winner == 'X' else RED
                draw_status(winner_text, color)
            else:
                draw_status("It's a Tie!", GREEN)
            
            # Draw restart button
            restart_button = pygame.Rect(150, WINDOW_SIZE + 20, 150, 60)
            menu_button = pygame.Rect(320, WINDOW_SIZE + 20, 150, 60)
            draw_button("Restart", restart_button, GREEN)
            draw_button("Menu", menu_button, GRAY)
        else:
            draw_status(status_text)
        
        pygame.display.flip()
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # Exit game
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                if current_player == 'X':
                    cell = get_cell_from_mouse(event.pos)
                    if cell is not None and game.make_move(cell, 'X'):
                        if game.current_winner:
                            game_over = True
                        elif not game.empty_squares():
                            game_over = True
                        else:
                            current_player = 'O'
                            status_text = "Player O's Turn" if game_mode == "pvp" else "Computer's Turn"
            elif event.type == pygame.MOUSEBUTTONDOWN and game_over:
                # Check restart/menu buttons
                restart_button = pygame.Rect(150, WINDOW_SIZE + 20, 150, 60)
                menu_button = pygame.Rect(320, WINDOW_SIZE + 20, 150, 60)
                if restart_button.collidepoint(event.pos):
                    return True  # Restart
                elif menu_button.collidepoint(event.pos):
                    return "menu"  # Go to menu
        
        # Computer's turn
        if not game_over and current_player == 'O' and o_player is not None:
            pygame.time.wait(500)  # Brief pause for better UX
            move = o_player.get_move(game)
            game.make_move(move, 'O')
            if game.current_winner:
                game_over = True
            elif not game.empty_squares():
                game_over = True
            else:
                current_player = 'X'
                status_text = "Your Turn (X)" if game_mode != "pvp" else "Player X's Turn"
        
        clock.tick(60)
    
    return False


def main():
    """Main function"""
    running = True
    
    while running:
        game_mode = show_menu()
        
        if game_mode is None:
            break
        
        result = play_game(game_mode)
        
        if result == False:  # Quit
            break
        elif result == True:  # Restart same mode
            continue
        elif result == "menu":  # Back to menu
            continue
    
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
