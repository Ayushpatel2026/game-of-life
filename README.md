# Game of Life

This is an object-oriented implementation of Conway's Game of Life in Python, showcasing algorithmic thinking and clean code design. 
The project is entirely condition-free, relying on object-oriented principles to handle the game logic. Unit tests are included to ensure functionality.

## Game of Life

The Game of Life is a cellular automaton devised by the mathematician John Conway. It consists of a grid of cells, where each cell can be either alive (X) or dead (_). 
The grid evolves over discrete time steps (generations) based on the following rules:
- **Underpopulation**: Any live cell with fewer than two live neighbors dies.
- **Survival**: Any live cell with two or three live neighbors survives.
- **Overpopulation**: Any live cell with more than three live neighbors dies.
- **Reproduction**: Any dead cell with exactly three live neighbors becomes a live cell.

## Features
- **Object-Oriented Design**: The game logic is fully encapsulated within classes, showcasing clean code practices and principles of object-oriented programming.
- **Condition-Free Logic**: I made this project without traditional `if`-statements or conditionals, and instead relying on delegation of tasks to different objects to implement the logic. 
- **Easy-to-Run Worlds**: Users can easily test different Game of Life configurations by creating new text files and running them through the game.
- **Unit Tests**: The project includes unit tests to verify the behavior of the game and its components.

## Getting Started

### Prerequisites
- Python 3.x installed on your machine.
  
### Install and Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Ayushpatel2026/game-of-life.git
   cd game-of-life
   ```
2. **Run the project**
   Specify the input text file and the number of generations to run
   ```bash
   python main.py worlds/example1.txt 6

### Input File Format

Input files should contain a grid of the world. The first line contains the dimension of the square grid:
- X represents a live cell
- _ represents a dead cell
**Example**
```
5
_ _ _ _ _
_ _ X _ _
_ _ _ X _
_ X X X _
_ _ _ _ _
```

### Adding New World Configurations
To test a new world configuration, simply create a new .txt file with the desired initial world state and specify it when running the command.
   
