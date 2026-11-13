# Lazor-Project
EN.540.635 Software Carpentry: Lazor Group Project

## Project Overview

The objective of this project is to create a general solver for the *Lazors* game. The program takes a puzzle as input and determines how to arrange the movable blocks so that the lasers intersect all required target points.

The solver supports three types of blocks: reflective (solid) blocks, opaque (stopper) blocks, and refractive (clear) blocks. It can also account for multiple lasers and both movable and fixed blocks. 

## How to Run

1. Place `.bff` puzzle files in the project folder
2. With project folder open in terminal, run the following command (replace `[filename].bff` with the name of your .bff file):

   ```bash
   python solve.py [filename].bff
   ```

4. If a solution is found, the program will print the block placements in the terminal and generate a text file showing the solved board.
5. If no solution is found, the terminal will display `No solution found.`

## Input and Output

### Input

The solver accepts `.bff` files that must contain the following information in this specified order: Grid layout, available squares, block types and quantities, fixed block locations, laser starting positions and directions, and target points. Incomplete or invalid information will raise an exception with an error message indicating what is missing or wrong with the file.

The grid begins with `GRID START` and ends with `GRID STOP`.

The following symbols are used:

- `o`: Empty square where a movable block can be placed.
- `x`: Unavailable square where a block cannot be placed.
- `A`: Reflective block.
- `B`: Opaque block.
- `C`: Refractive block.

Blocks represented by `A`, `B`, or `C` within the original grid are fixed and cannot be moved. Blocks specified after `GRID STOP`, such as `A 4`, indicate the number and type of movable blocks available.

Laser information is represented by `L x y vx vy`, where `x` and `y` specify the starting position and `vx` and `vy` specify the direction.

Target points are represented by `P x y`.

Coordinates are measured in half-block increments, with each half-block being equal to one step. The origin is at the top-left corner of the grid, with the positive axes pointing right and down. 

### Output

If the solver finds a valid solution, it generates a text file named `[puzzle_name]_solution.txt`.

The file contains a grid showing the final arrangement of blocks, along with a key explaining the grid symbols (same as above in 'Input') and instructions explaining how to use the solved board. 

If no solution is found, the program prints a message in the terminal instead of generating a solution file.

## File Descriptions

### `bffreader.py`

This file takes as input a `.bff` file, which contains information regarding the level in the game (grid layout, available squares on the grid, block types and locations, laser starting points and directions, and the points the lasers must intersect).

It reads the file and removes all comments and blank lines, leaving only the required information. It then parses the `.bff` file, organizing the relevant information into lists and dictionaries that can be retrieved by other files.

### `blockclasses.py`

This file defines the block classes for the solver. There are three different types of blocks (reflective, refractive, and opaque), and each has its own behavior.

Reflective blocks change the direction of the laser, opaque blocks stop the laser, and refractive blocks both reflect and transmit the laser.

### `laser.py`

This file defines the laser behavior for the puzzle. It uses the grid representation and laser information captured from `bffreader.py`, along with the block behaviors defined in `blockclasses.py`.

It simulates the movement of the lasers through the board, accounting for their interactions with different blocks. It also identifies the squares the lasers encounter and checks which target points have been reached.

### `solutionlogic.py`

This file contains the logic used to solve the puzzle. It uses a recursive depth-first search algorithm to test different arrangements of movable blocks.

The solver places blocks in available positions, simulates the resulting laser paths, and checks whether all target points have been reached. If a placement does not produce a solution, the solver backtracks and tries another arrangement.

The puzzle is considered solved when all target points have been reached by the lazor(s) and all required movable blocks have been placed.

### `output.py`

This file generates a text file containing the solved board. It creates a copy of the original grid and adds the movable blocks in the positions determined by the solver.

The output file also contains a key explaining the different grid symbols and instructions for interpreting the solution.

### `solve.py`

This is the main file used to run the program. It accepts a `.bff` filename from the terminal, retrieves the puzzle information using `bffreader.py`, and passes that information to `solutionlogic.py`.

If a solution is found, it calls `output.py` to generate a text file containing the completed board. It also handles cases where no input file is specified, the specified file cannot be found, or no solution is found.

### `test_bff_reader.py`

This file contains tests for `bffreader.py` to verify that the program correctly reads and interprets the information provided in `.bff` files. To run, open folder in terminal and enter:
   python test_bff_reader.py

### `testlaser.py`

This file tests laser.py and the block classes in blockclasses.py by checking that the laser bounces off the different block types as intended. To run, enter from terminal:
   python testlaser.py

### `testsolver.py`
Test solver.py by making sure it gives the intended output (check_win=True) for example.bff. To run, open folder in terminal and enter: 
   python testsolver.py

## Authors

- Amber Alkadry
- Caleb Medina

Johns Hopkins University — EN.540.635 Software Carpentry, Fall 2026
