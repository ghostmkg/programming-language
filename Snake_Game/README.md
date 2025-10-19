# Snake Game - Classic Arcade Experience 🐍

A modern, feature-rich implementation of the classic Snake game built with Python and Pygame. Experience the nostalgia of arcade gaming with enhanced graphics, multiple difficulty levels, and smooth gameplay.

## Features

- 🎮 **Classic Gameplay**: Traditional Snake game mechanics with modern enhancements
- 🎯 **Multiple Difficulty Levels**: Easy, Medium, and Hard modes
- 🏆 **Score System**: Track your score and compete for high scores
- 📊 **Level Progression**: Speed increases as you advance through levels
- 🍎 **Special Food Types**: Normal, bonus, and special food with different point values
- ⏸️ **Pause Functionality**: Pause and resume gameplay anytime
- 🎨 **Beautiful Graphics**: Smooth animations and colorful visuals
- 💾 **High Score Persistence**: Your best scores are saved automatically
- 🎵 **Sound Effects**: Optional audio feedback (can be extended)

## Installation

### Prerequisites
- Python 3.6 or higher
- Pygame library

### Setup
```bash
# Clone the repository
git clone <repository-url>
cd Snake_Game

# Install Pygame
pip install pygame

# Run the game
python snake_game.py
```

### Alternative Installation
```bash
# Using pip with requirements
pip install -r requirements.txt
python snake_game.py
```

## How to Play

### Basic Controls
- **Arrow Keys** or **WASD**: Move the snake
- **Space**: Pause/Resume game
- **ESC**: Return to main menu or exit
- **R**: Restart game (when game over)
- **H**: View high scores

### Game Rules
1. Control the snake to eat food and grow longer
2. Avoid hitting walls or your own body
3. Different food types give different points:
   - **Red Food**: 10 points (normal)
   - **Yellow Food**: 25 points (bonus)
   - **Purple Food**: 50 points (special)
4. Speed increases every 50 points (new level)
5. Try to achieve the highest score possible!

### Difficulty Levels
- **Easy**: Slower speed, more forgiving gameplay
- **Medium**: Balanced speed and challenge (default)
- **Hard**: Faster speed, more challenging gameplay

## Game Features

### Visual Elements
- **Snake Head**: Dark green with white border
- **Snake Body**: Bright green segments
- **Food Types**: Different colors and effects
- **UI Elements**: Score, high score, level display
- **Smooth Animations**: Fluid movement and transitions

### Scoring System
- **Normal Food**: 10 points
- **Bonus Food**: 25 points
- **Special Food**: 50 points
- **Level Bonus**: Speed increases every 50 points
- **High Score**: Automatically saved and displayed

### Game States
- **Main Menu**: Choose difficulty and view options
- **Playing**: Active gameplay
- **Paused**: Game paused, can resume
- **Game Over**: Final score and restart options
- **High Scores**: View your best performance

## Technical Details

### Architecture
- **Object-Oriented Design**: Clean, modular code structure
- **State Management**: Proper game state handling
- **Event-Driven**: Responsive input handling
- **Performance Optimized**: Smooth 60 FPS gameplay

### File Structure
```
Snake_Game/
├── snake_game.py          # Main game file
├── README.md             # This documentation
├── requirements.txt      # Dependencies
└── high_score.json       # High score storage (auto-generated)
```

### Dependencies
- **pygame**: Game development library
- **json**: High score persistence
- **random**: Food placement
- **sys**: System operations
- **os**: File operations

## Customization

### Easy Modifications
- **Colors**: Change color scheme in constants section
- **Speed**: Adjust initial speed and level progression
- **Grid Size**: Modify GRID_SIZE for different resolutions
- **Food Types**: Add new food types with custom behaviors
- **Scoring**: Adjust point values for different food types

### Advanced Customization
- **Sound Effects**: Add audio with pygame.mixer
- **Power-ups**: Implement special abilities
- **Multiplayer**: Add two-player mode
- **Themes**: Create different visual themes
- **Mobile Support**: Adapt for touch controls

## Troubleshooting

### Common Issues
1. **Pygame not found**: Install with `pip install pygame`
2. **Game runs too fast/slow**: Adjust speed settings in code
3. **Controls not responsive**: Check for conflicting key mappings
4. **High score not saving**: Ensure write permissions in game directory

### Performance Tips
- Close other applications for better performance
- Use fullscreen mode for smoother gameplay
- Adjust speed settings if game feels sluggish

## Contributing

Contributions are welcome! Areas for improvement:
- **New Features**: Power-ups, obstacles, multiplayer
- **Visual Enhancements**: Better graphics, animations, effects
- **Audio**: Sound effects and background music
- **Mobile Support**: Touch controls and mobile optimization
- **AI Mode**: Computer-controlled snake opponent
- **Level Editor**: Custom level creation tools

## Future Enhancements

- **Multiplayer Mode**: Local and online multiplayer
- **Power-ups**: Speed boost, invincibility, score multiplier
- **Obstacles**: Walls and barriers to navigate
- **Themes**: Multiple visual themes and skins
- **Achievements**: Unlockable achievements and rewards
- **Statistics**: Detailed gameplay statistics and analytics

## License

This project is open source and available under the MIT License.

---

**Enjoy the classic Snake experience with modern enhancements!** 🐍🎮

Try to beat your high score and challenge your friends!
