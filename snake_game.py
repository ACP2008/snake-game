import pygame
import random
import sys
from enum import Enum
from collections import deque

# Initialize Pygame
pygame.init()

# Colors
COLOR_BLACK = (10, 10, 10)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (34, 177, 76)
COLOR_DARK_GREEN = (0, 120, 0)
COLOR_RED = (231, 76, 60)
COLOR_YELLOW = (241, 196, 15)
COLOR_GOLD = (255, 215, 0)
COLOR_BLUE = (52, 152, 219)
COLOR_PURPLE = (155, 89, 182)
COLOR_CYAN = (26, 188, 156)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Game speed
CLOCK_TICK = 10

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

class SnakeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("🐍 Snake Game - Python Edition")
        self.clock = pygame.time.Clock()
        self.font_large = pygame.font.Font(None, 72)
        self.font_medium = pygame.font.Font(None, 48)
        self.font_small = pygame.font.Font(None, 32)
        self.font_tiny = pygame.font.Font(None, 24)
        
        self.reset_game()
    
    def reset_game(self):
        """Reset game to initial state"""
        # Start snake in the middle
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2
        self.snake = deque([(start_x, start_y), (start_x - 1, start_y), (start_x - 2, start_y)])
        self.direction = Direction.RIGHT
        self.next_direction = Direction.RIGHT
        self.food = self.spawn_food()
        self.score = 0
        self.game_over = False
    
    def spawn_food(self):
        """Spawn food at random location not occupied by snake"""
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in self.snake:
                return (x, y)
    
    def handle_input(self):
        """Handle keyboard input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != Direction.DOWN:
                    self.next_direction = Direction.UP
                elif event.key == pygame.K_DOWN and self.direction != Direction.UP:
                    self.next_direction = Direction.DOWN
                elif event.key == pygame.K_LEFT and self.direction != Direction.RIGHT:
                    self.next_direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT and self.direction != Direction.LEFT:
                    self.next_direction = Direction.RIGHT
                elif event.key == pygame.K_SPACE and self.game_over:
                    self.reset_game()
                elif event.key == pygame.K_ESCAPE:
                    return False
        return True
    
    def update(self):
        """Update game state"""
        if self.game_over:
            return
        
        self.direction = self.next_direction
        
        # Calculate new head position
        head_x, head_y = self.snake[0]
        dx, dy = self.direction.value
        new_head = (head_x + dx, head_y + dy)
        
        # Check wall collision
        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or 
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
            self.game_over = True
            return
        
        # Check self collision
        if new_head in self.snake:
            self.game_over = True
            return
        
        # Add new head
        self.snake.appendleft(new_head)
        
        # Check food collision
        if new_head == self.food:
            self.score += 10
            self.food = self.spawn_food()
        else:
            self.snake.pop()
    
    def draw(self):
        """Draw game elements"""
        self.screen.fill(COLOR_BLACK)
        
        # Draw grid (subtle)
        for x in range(0, SCREEN_WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, (30, 30, 30), (x, 0), (x, SCREEN_HEIGHT), 1)
        for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, (30, 30, 30), (0, y), (SCREEN_WIDTH, y), 1)
        
        # Draw snake
        for i, (x, y) in enumerate(self.snake):
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE - 2, GRID_SIZE - 2)
            if i == 0:  # Head
                pygame.draw.rect(self.screen, COLOR_CYAN, rect)
                pygame.draw.rect(self.screen, COLOR_BLUE, rect, 3)
            else:  # Body
                color = COLOR_GREEN if i % 2 == 0 else COLOR_DARK_GREEN
                pygame.draw.rect(self.screen, color, rect)
        
        # Draw food
        food_x, food_y = self.food
        food_rect = pygame.Rect(food_x * GRID_SIZE + 2, food_y * GRID_SIZE + 2, GRID_SIZE - 4, GRID_SIZE - 4)
        pygame.draw.circle(self.screen, COLOR_RED, 
                          (food_x * GRID_SIZE + GRID_SIZE // 2, food_y * GRID_SIZE + GRID_SIZE // 2), 
                          GRID_SIZE // 2 - 2)
        pygame.draw.circle(self.screen, COLOR_GOLD, 
                          (food_x * GRID_SIZE + GRID_SIZE // 2, food_y * GRID_SIZE + GRID_SIZE // 2), 
                          GRID_SIZE // 2 - 3, 2)
        
        # Draw score
        score_text = self.font_small.render(f"Score: {self.score}", True, COLOR_YELLOW)
        self.screen.blit(score_text, (10, 10))
        
        # Draw high score or game over message
        if self.game_over:
            # Semi-transparent overlay
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(128)
            overlay.fill(COLOR_BLACK)
            self.screen.blit(overlay, (0, 0))
            
            # Game Over text
            game_over_text = self.font_large.render("GAME OVER", True, COLOR_RED)
            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
            self.screen.blit(game_over_text, game_over_rect)
            
            # Final score
            final_score_text = self.font_medium.render(f"Final Score: {self.score}", True, COLOR_GOLD)
            final_score_rect = final_score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(final_score_text, final_score_rect)
            
            # Restart instruction
            restart_text = self.font_small.render("Press SPACE to Restart or ESC to Quit", True, COLOR_CYAN)
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
            self.screen.blit(restart_text, restart_rect)
        else:
            # Instructions
            instruction_text = self.font_tiny.render("Use Arrow Keys to Move", True, COLOR_WHITE)
            self.screen.blit(instruction_text, (SCREEN_WIDTH - 250, 10))
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        running = True
        while running:
            running = self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(CLOCK_TICK)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
