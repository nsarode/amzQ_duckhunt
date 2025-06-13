# Duck Hunt Game

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
