# Duck Hunt Game

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![Ursina Engine](https://img.shields.io/badge/Ursina-Engine-orange)](https://www.ursinaengine.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)](https://www.docker.com/)
[![Amazon Q](https://img.shields.io/badge/Built%20with-Amazon%20Q-FF9900?logo=amazon)](https://aws.amazon.com/q/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub issues](https://img.shields.io/github/issues/nsarode/amzQ_duckhunt)](https://github.com/nsarode/amzQ_duckhunt/issues)

A modern implementation of the classic Duck Hunt game using the Ursina game engine.

## Features

- First-person duck hunting gameplay
- Score tracking and high score system
- Time-limited rounds with increasing difficulty
- Visual feedback for hits and misses
- Simple 3D environment

## Controls

- Mouse movement: Aim
- Left mouse button: Shoot
- ESC key: Pause/Menu
- R key: Restart game
- F9/F10: Increase/Decrease window size
- F11: Toggle fullscreen
- Ctrl+Q or Shift+Q: Emergency exit

## Requirements

- Python 3.x
- Ursina game engine (`pip install ursina`)

## Installation

### Option 1: Direct Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nsarode/amzQ_duckhunt.git
   cd amzQ_duckhunt
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the game:
   ```bash
   python duck_hunt.py
   ```

### Option 2: Docker Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nsarode/amzQ_duckhunt.git
   cd amzQ_duckhunt
   ```

2. Build and run with Docker:
   ```bash
   docker-compose up --build
   ```

#### X11 Forwarding for Docker (Linux)

For Linux hosts, you need to allow X11 connections:

```bash
xhost +local:docker
docker-compose up
```

#### X11 Forwarding for Docker (Mac/Windows)

For Mac or Windows, additional setup is required:

- **Mac**: Install XQuartz and run:
  ```bash
  xhost +localhost
  docker-compose up
  ```

- **Windows**: Install VcXsrv or Xming, then set DISPLAY environment variable.

## Development

- The game is built with the Ursina game engine
- High scores are saved in `duck_hunt_high_score.json`
- Modify `duck_hunt.py` to add new features or change game mechanics

## Future Improvements

For Python developers looking to enhance this project, consider the following improvements:

- **Game Engine Alternatives**: Evaluate other Python game engines like PyGame, Panda3D, or Arcade for better performance or specific features
- **Sound Implementation**: Add sound effects by:
  - Creating/acquiring WAV files for shoot, hit, miss, and quack sounds
  - Placing them in the root directory (referenced in the code)
  - Implementing volume control and audio mixing
- **Asset Pipeline**: Create a proper asset loading system with fallbacks for missing resources
- **Performance Optimization**: Profile the game loop and optimize rendering for smoother mouse response
- **Duck AI**: Implement more sophisticated movement patterns using path finding or behavior trees
- **Level System**: Add progressive difficulty levels with different environments and duck behaviors
- **Multiplayer Support**: Implement local or network multiplayer using Python's networking libraries
- **Custom Shader Support**: Implement custom shaders for water effects, dynamic lighting, etc.
- **Unit Testing**: Add pytest-based unit tests for game logic components
- **Save/Load System**: Implement a more robust save system using SQLite or pickle
- **Controller Support**: Add gamepad/controller support using the pygame.joystick module
- **Code Refactoring**: Reorganize into a proper package structure with separate modules for:
  - Entity classes
  - UI components
  - Game states
  - Asset management
- **Documentation**: Generate API documentation using Sphinx or pdoc
