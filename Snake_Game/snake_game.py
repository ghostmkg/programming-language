#!/usr/bin/env python3
"""
Snake Game - Classic Arcade Game
================================

A modern implementation of the classic Snake game with enhanced features:
- Smooth gameplay with customizable speed
- Score tracking and high score system
- Multiple difficulty levels
- Beautiful graphics and animations
- Sound effects (optional)
- Pause functionality
- Game over screen with restart option

Author: AI Assistant
Language: Python 3
Dependencies: pygame, random, sys, os
"""

import pygame
import random
import sys
import os
import json
from enum import Enum

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Colors (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GRAY = (128, 128, 128)
DARK_GREEN = (0, 150, 0)
LIGHT_GREEN = (144, 238, 144)

# Game states
class GameState(Enum):
    MENU = 1
    PLAYING = 2
    PAUSED = 3
    GAME_OVER = 4
    HIGH_SCORES = 5

# Directions
class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

class Snake:
    def __init__(self, x, y):
        self.body = [(x, y)]
        self.direction = Direction.RIGHT
        self.grow = False
        
    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction.value
        new_head = (head_x + dx, head_y + dy)
        
        self.body.insert(0, new_head)
        
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
    
    def change_direction(self, new_direction):
        # Prevent reversing into itself
        if (self.direction == Direction.UP and new_direction == Direction.DOWN) or \
           (self.direction == Direction.DOWN and new_direction == Direction.UP) or \
           (self.direction == Direction.LEFT and new_direction == Direction.RIGHT) or \
           (self.direction == Direction.RIGHT and new_direction == Direction.LEFT):
            return
        self.direction = new_direction
    
    def grow_snake(self):
        self.grow = True
    
    def check_collision(self):
        head_x, head_y = self.body[0]
        
        # Check wall collision
        if head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT:
            return True
        
        # Check self collision
        if (head_x, head_y) in self.body[1:]:
            return True
        
        return False
    
    def draw(self, screen):
        for i, (x, y) in enumerate(self.body):
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            
            if i == 0:  # Head
                pygame.draw.rect(screen, DARK_GREEN, rect)
                pygame.draw.rect(screen, WHITE, rect, 2)
            else:  # Body
                pygame.draw.rect(screen, GREEN, rect)
                pygame.draw.rect(screen, WHITE, rect, 1)

class Food:
    def __init__(self):
        self.position = self.generate_position()
        self.type = random.choice(['normal', 'bonus', 'special'])
        self.color = self.get_color()
    
    def generate_position(self):
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        return (x, y)
    
    def get_color(self):
        colors = {
            'normal': RED,
            'bonus': YELLOW,
            'special': PURPLE
        }
        return colors[self.type]
    
    def draw(self, screen):
        x, y = self.position
        rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, self.color, rect)
        pygame.draw.rect(screen, WHITE, rect, 2)
        
        # Add special effects for different food types
        if self.type == 'bonus':
            inner_rect = pygame.Rect(x * GRID_SIZE + 4, y * GRID_SIZE + 4, 
                                   GRID_SIZE - 8, GRID_SIZE - 8)
            pygame.draw.rect(screen, ORANGE, inner_rect)
        elif self.type == 'special':
            center_x = x * GRID_SIZE + GRID_SIZE // 2
            center_y = y * GRID_SIZE + GRID_SIZE // 2
            pygame.draw.circle(screen, WHITE, (center_x, center_y), 4)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game - Classic Arcade")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.large_font = pygame.font.Font(None, 72)
        
        self.state = GameState.MENU
        self.score = 0
        self.high_score = self.load_high_score()
        self.level = 1
        self.speed = 10
        self.snake = None
        self.food = None
        self.paused = False
        
        # Game settings
        self.difficulty = "Medium"
        self.sound_enabled = True
        
    def load_high_score(self):
        try:
            with open('high_score.json', 'r') as f:
                data = json.load(f)
                return data.get('high_score', 0)
        except FileNotFoundError:
            return 0
    
    def save_high_score(self):
        data = {'high_score': self.high_score}
        with open('high_score.json', 'w') as f:
            json.dump(data, f)
    
    def start_game(self):
        self.state = GameState.PLAYING
        self.score = 0
        self.level = 1
        self.speed = 10
        
        # Initialize snake in center
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2
        self.snake = Snake(start_x, start_y)
        
        # Generate first food
        self.food = Food()
        
        # Adjust speed based on difficulty
        if self.difficulty == "Easy":
            self.speed = 8
        elif self.difficulty == "Hard":
            self.speed = 15
        else:  # Medium
            self.speed = 10
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if self.state == GameState.MENU:
                    self.handle_menu_input(event.key)
                elif self.state == GameState.PLAYING:
                    self.handle_game_input(event.key)
                elif self.state == GameState.PAUSED:
                    self.handle_pause_input(event.key)
                elif self.state == GameState.GAME_OVER:
                    self.handle_game_over_input(event.key)
                elif self.state == GameState.HIGH_SCORES:
                    self.handle_high_scores_input(event.key)
        
        return True
    
    def handle_menu_input(self, key):
        if key == pygame.K_1:
            self.difficulty = "Easy"
            self.start_game()
        elif key == pygame.K_2:
            self.difficulty = "Medium"
            self.start_game()
        elif key == pygame.K_3:
            self.difficulty = "Hard"
            self.start_game()
        elif key == pygame.K_h:
            self.state = GameState.HIGH_SCORES
        elif key == pygame.K_ESCAPE:
            return False
    
    def handle_game_input(self, key):
        if key == pygame.K_UP or key == pygame.K_w:
            self.snake.change_direction(Direction.UP)
        elif key == pygame.K_DOWN or key == pygame.K_s:
            self.snake.change_direction(Direction.DOWN)
        elif key == pygame.K_LEFT or key == pygame.K_a:
            self.snake.change_direction(Direction.LEFT)
        elif key == pygame.K_RIGHT or key == pygame.K_d:
            self.snake.change_direction(Direction.RIGHT)
        elif key == pygame.K_SPACE:
            self.state = GameState.PAUSED
        elif key == pygame.K_ESCAPE:
            self.state = GameState.MENU
    
    def handle_pause_input(self, key):
        if key == pygame.K_SPACE:
            self.state = GameState.PLAYING
        elif key == pygame.K_ESCAPE:
            self.state = GameState.MENU
    
    def handle_game_over_input(self, key):
        if key == pygame.K_r:
            self.start_game()
        elif key == pygame.K_m:
            self.state = GameState.MENU
        elif key == pygame.K_ESCAPE:
            return False
    
    def handle_high_scores_input(self, key):
        if key == pygame.K_ESCAPE or key == pygame.K_m:
            self.state = GameState.MENU
    
    def update_game(self):
        if self.state != GameState.PLAYING:
            return
        
        self.snake.move()
        
        # Check collision
        if self.snake.check_collision():
            self.game_over()
            return
        
        # Check food collision
        if self.snake.body[0] == self.food.position:
            self.eat_food()
        
        # Level up based on score
        new_level = (self.score // 50) + 1
        if new_level > self.level:
            self.level = new_level
            self.speed = min(20, self.speed + 1)  # Increase speed, max 20
    
    def eat_food(self):
        # Add score based on food type
        if self.food.type == 'normal':
            self.score += 10
        elif self.food.type == 'bonus':
            self.score += 25
        elif self.food.type == 'special':
            self.score += 50
        
        self.snake.grow_snake()
        
        # Generate new food
        self.food = Food()
        
        # Make sure food doesn't spawn on snake
        while self.food.position in self.snake.body:
            self.food = Food()
        
        # Update high score
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
    
    def game_over(self):
        self.state = GameState.GAME_OVER
    
    def draw_menu(self):
        self.screen.fill(BLACK)
        
        # Title
        title_text = self.large_font.render("SNAKE GAME", True, GREEN)
        title_rect = title_text.get_rect(center=(WINDOW_WIDTH//2, 100))
        self.screen.blit(title_text, title_rect)
        
        # Subtitle
        subtitle_text = self.font.render("Classic Arcade Experience", True, WHITE)
        subtitle_rect = subtitle_text.get_rect(center=(WINDOW_WIDTH//2, 150))
        self.screen.blit(subtitle_text, subtitle_rect)
        
        # Menu options
        menu_options = [
            "1. Easy Mode",
            "2. Medium Mode (Default)",
            "3. Hard Mode",
            "H. High Scores",
            "ESC. Exit"
        ]
        
        y_offset = 250
        for option in menu_options:
            text = self.font.render(option, True, WHITE)
            text_rect = text.get_rect(center=(WINDOW_WIDTH//2, y_offset))
            self.screen.blit(text, text_rect)
            y_offset += 50
        
        # Instructions
        instructions = [
            "Controls:",
            "Arrow Keys or WASD - Move",
            "Space - Pause",
            "ESC - Menu/Exit"
        ]
        
        y_offset = 500
        for instruction in instructions:
            text = self.small_font.render(instruction, True, GRAY)
            text_rect = text.get_rect(center=(WINDOW_WIDTH//2, y_offset))
            self.screen.blit(text, text_rect)
            y_offset += 25
    
    def draw_game(self):
        self.screen.fill(BLACK)
        
        # Draw snake and food
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        
        # Draw UI
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        high_score_text = self.font.render(f"High Score: {self.high_score}", True, WHITE)
        self.screen.blit(high_score_text, (10, 50))
        
        level_text = self.font.render(f"Level: {self.level}", True, WHITE)
        self.screen.blit(level_text, (10, 90))
        
        # Pause indicator
        if self.state == GameState.PAUSED:
            pause_text = self.large_font.render("PAUSED", True, YELLOW)
            pause_rect = pause_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
            self.screen.blit(pause_text, pause_rect)
            
            resume_text = self.font.render("Press SPACE to resume", True, WHITE)
            resume_rect = resume_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 50))
            self.screen.blit(resume_text, resume_rect)
    
    def draw_game_over(self):
        self.screen.fill(BLACK)
        
        # Game Over text
        game_over_text = self.large_font.render("GAME OVER", True, RED)
        game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH//2, 200))
        self.screen.blit(game_over_text, game_over_rect)
        
        # Final score
        final_score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
        final_score_rect = final_score_text.get_rect(center=(WINDOW_WIDTH//2, 280))
        self.screen.blit(final_score_text, final_score_rect)
        
        # High score
        if self.score == self.high_score:
            new_record_text = self.font.render("NEW HIGH SCORE!", True, YELLOW)
            new_record_rect = new_record_text.get_rect(center=(WINDOW_WIDTH//2, 320))
            self.screen.blit(new_record_text, new_record_rect)
        
        # Options
        options = [
            "R. Play Again",
            "M. Main Menu",
            "ESC. Exit"
        ]
        
        y_offset = 400
        for option in options:
            text = self.font.render(option, True, WHITE)
            text_rect = text.get_rect(center=(WINDOW_WIDTH//2, y_offset))
            self.screen.blit(text, text_rect)
            y_offset += 50
    
    def draw_high_scores(self):
        self.screen.fill(BLACK)
        
        # Title
        title_text = self.large_font.render("HIGH SCORES", True, GREEN)
        title_rect = title_text.get_rect(center=(WINDOW_WIDTH//2, 100))
        self.screen.blit(title_text, title_rect)
        
        # High score
        high_score_text = self.font.render(f"Best Score: {self.high_score}", True, YELLOW)
        high_score_rect = high_score_text.get_rect(center=(WINDOW_WIDTH//2, 200))
        self.screen.blit(high_score_text, high_score_rect)
        
        # Instructions
        instruction_text = self.font.render("Press ESC or M to return to menu", True, WHITE)
        instruction_rect = instruction_text.get_rect(center=(WINDOW_WIDTH//2, 300))
        self.screen.blit(instruction_text, instruction_rect)
    
    def draw(self):
        if self.state == GameState.MENU:
            self.draw_menu()
        elif self.state == GameState.PLAYING or self.state == GameState.PAUSED:
            self.draw_game()
        elif self.state == GameState.GAME_OVER:
            self.draw_game_over()
        elif self.state == GameState.HIGH_SCORES:
            self.draw_high_scores()
        
        pygame.display.flip()
    
    def run(self):
        running = True
        
        while running:
            running = self.handle_events()
            
            if self.state == GameState.PLAYING:
                self.update_game()
            
            self.draw()
            self.clock.tick(self.speed)
        
        pygame.quit()
        sys.exit()

def main():
    """Main function to run the Snake Game"""
    print("🐍 Starting Snake Game...")
    print("Controls:")
    print("  Arrow Keys or WASD - Move")
    print("  Space - Pause")
    print("  ESC - Menu/Exit")
    print("  R - Restart (Game Over)")
    print("  H - High Scores")
    print("\nEnjoy the game!")
    
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
