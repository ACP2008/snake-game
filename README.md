# 🐍 Snake Game - Python Edition

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Pygame](https://img.shields.io/badge/Pygame-2.5%2B-green?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge)

**A colorful, modern implementation of the classic Snake game built with Python and Pygame!** 🎮

[Play Game](#-how-to-play) • [Installation](#-installation) • [Features](#-features) • [Contributing](#-contributing)

</div>

---

## ✨ Features

### 🎨 Vibrant Visual Design
- 🌈 Beautiful gradient color scheme with cyan heads and green bodies
- ✨ Glowing effects on food with gold accents
- 🎪 Smooth animations and visual feedback
- 📊 Real-time score display with modern UI
- 🎭 Semi-transparent game over overlay

### 🎯 Gameplay Elements
- 🐍 Smooth snake movement and controls
- 🍎 Randomly spawned food pellets
- 📈 Score tracking system (10 points per food)
- 🎪 Intelligent collision detection
- 🔄 Quick restart functionality with SPACE key
- ⚡ Smooth 10 FPS gameplay for optimal control

### 🖥️ User Interface
- 💻 Clean, modern UI with clear instructions
- 🎯 Intuitive arrow key controls
- 📱 Responsive game window (800x600)
- 🎪 Game over overlay with restart option
- 📝 On-screen controls display

---

## 📋 Requirements

- **Python**: 3.8 or higher
- **Pygame**: 2.5 or higher
- **RAM**: 256 MB minimum
- **Display**: 800x600 minimum resolution
- **OS**: Windows, macOS, or Linux

---

## 🚀 Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/ACP2008/snake-game.git
cd snake-game
```

### Step 2: Create Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Game
```bash
python snake_game.py
```

---

## 🎮 How to Play

### Controls

| Key | Action | Description |
|-----|--------|-------------|
| ⬆️ **UP** | Move Up | Move snake toward the top |
| ⬇️ **DOWN** | Move Down | Move snake toward the bottom |
| ⬅️ **LEFT** | Move Left | Move snake to the left |
| ➡️ **RIGHT** | Move Right | Move snake to the right |
| **SPACE** | Restart | Restart game after game over |
| **ESC** | Quit | Exit the game |

### Objective

🎯 **Guide your snake to eat the food while avoiding obstacles:**

1. 🍎 Eat the red food pellets to grow and score points
2. 🧱 Avoid hitting the walls (screen boundaries)
3. 🐍 Avoid colliding with your own body
4. 📈 Achieve the highest score possible

### Scoring System

- 🍎 Each food eaten = **+10 points**
- 📈 The longer your snake, the higher your potential score
- 🏆 Try to beat your personal best!

---

## 🎨 Color Scheme

The game features a beautiful, carefully chosen color palette:

```
🟦 Cyan (#1ABC9C)        - Snake Head (with blue border)
🟩 Green (#22B14C)       - Snake Body (Primary)
🟩 Dark Green (#007800)  - Snake Body (Alternate for pattern)
🔴 Red (#E74C3C)         - Food Pellet
🟨 Gold (#FFD700)        - Accent & Score Text
⬛ Black (#0A0A0A)       - Background
🔵 Blue (#3498DB)        - UI Accents & Head Border
⚪ White (#FFFFFF)       - Text & Instructions
```

---

## 📁 Project Structure

```
snake-game/
├── snake_game.py          # Main game file with all logic
├── requirements.txt       # Python dependencies
├── README.md             # This comprehensive guide
└── .gitignore           # Git ignore file (optional)
```

---

## 🔧 Technical Details

### Architecture

**SnakeGame Class** - Complete game controller

```python
class SnakeGame:
    __init__()        # Initialize pygame and game state
    reset_game()      # Reset to initial state
    spawn_food()      # Generate food at random location
    handle_input()    # Process keyboard events
    update()          # Update game state and physics
    draw()            # Render all graphics
    run()             # Main game loop
```

### Key Components

#### 1. **Game Loop** (10 FPS)
- Input handling (arrow keys, space, ESC)
- Game state updates (movement, collision)
- Rendering (graphics, text, UI)

#### 2. **Collision Detection**
- ⚠️ Wall collision (game over)
- ⚠️ Self collision (game over)
- ✅ Food collision (score +10)

#### 3. **Snake Movement**
- Smooth directional movement with deque
- Prevention of 180-degree turns
- Body tracking and rendering

#### 4. **Food System**
- Random spawn at valid locations
- Visual indicators with color and glow
- Collision detection with snake head

---

## 💡 Gameplay Tips & Strategies

### Tips for Better Scores:

1. **🎯 Plan Ahead**: Don't make sudden moves - think two steps ahead
2. **🌀 Create Loops**: Try to create spiral patterns to maximize space usage
3. **🎪 Avoid Corners**: Corners are dangerous - keep to the middle when possible
4. **🐍 Smooth Movement**: Avoid jerky movements, keep steady
5. **🧠 Use the Grid**: Use the visible grid lines as reference points
6. **⏱️ Control Speed**: Don't rush - the game moves at 10 FPS for control
7. **🗺️ Map Awareness**: Always know where the walls are
8. **📊 Score Tracking**: Set personal bests and try to beat them!

### Difficulty Progression:
- **Beginner**: Focus on just eating food
- **Intermediate**: Avoid collisions with walls
- **Advanced**: Plan complex patterns
- **Expert**: Achieve 200+ points!

---

## 🚀 Future Enhancements

Planned features for upcoming versions:

- [ ] 🎮 **Multiple Difficulty Levels** (Easy, Medium, Hard)
- [ ] 🏆 **High Score Leaderboard** (local save)
- [ ] 🎵 **Sound Effects & Background Music**
- [ ] ⚡ **Power-ups** (speed boost, temporary invincibility)
- [ ] 🌙 **Dark/Light Theme Toggle**
- [ ] 📱 **Mobile Touch Controls**
- [ ] 🎨 **Custom Snake Skins** (colors, patterns)
- [ ] 🗺️ **Different Map Variations** (obstacles, maze)
- [ ] 👥 **Multiplayer Mode** (local co-op)
- [ ] 📊 **Statistics & Analytics**

---

## 🐛 Troubleshooting

### Common Issues

**Problem**: "ModuleNotFoundError: No module named 'pygame'"
- **Solution**: Run `pip install -r requirements.txt`

**Problem**: "pygame.error: No available video device"
- **Solution**: Ensure you have a display connected or run in a graphical environment

**Problem**: Game runs but is very slow
- **Solution**: Check your system resources; close other applications

**Problem**: Arrow keys not responding
- **Solution**: Ensure the game window is in focus; try restarting

---

## 📄 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

```
MIT License

Copyright (c) 2024 ACP2008

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Ways to Contribute:
- 🐛 **Report Bugs**: Found an issue? Open a GitHub issue
- 💡 **Suggest Features**: Have an idea? Share it with us
- 🔧 **Submit Pull Requests**: Code improvements are always welcome
- 📝 **Improve Documentation**: Help make this guide better
- 🎨 **Design Improvements**: Suggest visual enhancements

### Development Setup:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

---

## 👨‍💻 Author

**ACP2008**
- GitHub: [@ACP2008](https://github.com/ACP2008)
- Repository: [snake-game](https://github.com/ACP2008/snake-game)

---

## 📞 Support

Need help? Follow these steps:

1. 📖 **Check Documentation**: Review this README thoroughly
2. 🔍 **Search Issues**: Check if your issue is already reported
3. 🔧 **Verify Setup**: Ensure Python and Pygame are correctly installed
4. 💾 **Check Dependencies**: Run `pip install -r requirements.txt` again
5. 🐛 **Report Issue**: Open a GitHub issue with details

---

## 🎮 Game Screenshots

### Gameplay
- Start with a small snake in the middle
- Green snake body with cyan head
- Red food pellets to eat
- Real-time score display
- Smooth grid-based movement

### Game Over Screen
- Semi-transparent overlay
- "GAME OVER" in large red text
- Final score displayed in gold
- Instructions to restart or quit

---

<div align="center">

### 🎮 Ready to Play? Start Now! 🐍

```bash
git clone https://github.com/ACP2008/snake-game.git
cd snake-game
pip install -r requirements.txt
python snake_game.py
```

⭐ **If you like this project, please give it a star on GitHub!** ⭐

```
     🐍🐍🐍
   🐍     🐍
 🐍       🐍
🐍         🐍
 🐍       🐍
   🐍   🐍
     🐍🐍
```

**Happy Gaming!** 🎮✨

[⬆ back to top](#-snake-game---python-edition)

</div>
