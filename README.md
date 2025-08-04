# Tic Tac Toe AI

Tic Tac Toe AI is a Python project that lets you play Tic Tac Toe against an AI using the minimax algorithm. It features a console-based interface and a modular codebase for easy extension.

## Features
- Play Tic Tac Toe in the console
- Challenge an AI powered by the minimax algorithm
- Modular code structure for easy customization

## Project Structure
```
frontend/         # Console interface and play script
  play.py         # Entry point to play the game
  console/        # CLI, player, and renderer modules
library/          # Core game logic and AI
  src/tic_tac_toe/game/      # Game engine, players, renderers
  src/tic_tac_toe/logic/     # Minimax AI, models, validators
```

## Installation
1. Clone this repository:
   ```sh
   git clone <repo-url>
   cd ai-tic-tac-toe
   ```
2. (Optional) Create and activate a virtual environment:
   ```sh
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```sh
   pip install -e ./library
   ```

## How to Play
Run the following command to start the game:
```sh
cd frontend
python -m console -X human|random|minimax -O human|random|minimax
```

## Requirements
- Python 3.8+
