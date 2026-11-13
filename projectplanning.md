# Lazor-Project
EN.540.635 Lazor Project

1. You must read in the Lazor board via a text file with a specific format (.bff). The specified file format will be further
elaborated below.
2. You must use a class object to describe the blocks within the game.
3. You must have an output file that shows the valid solution (text file, png image, etc). Output file format is up to you;
however, it must be easy to understand.
4. The code should NOT be slow. We have included various boards to use for benchmarking. [Will ask abt this tomorrow] We will be using these (and possibly others) to test out your code. Try to make it such that all the test boards are solved at a reasonable pace.
None of them should take more than 1 minute (some should be under 5 seconds); however, your code has 2 minutes to solve each individual board. If your solution of any single board takes more than 2 minutes, points will be deducted.
If your solution is absurdly fast for all boards, we may give bonus points!
your boards should allow for three types of blocks: (a) reflect blocks, (b) opaque blocks, and (c) refract blocks. Further,
you should also account for boards in which a block is fixed in a starting position.

Notes:
treat the lasers as rays? It seems they only ever reflect 90 degrees at a time, and the direction of reflection depends on block type and which side of the block it hit. 

Things we'll need:
Define block classes (what each block type is, the geometry of how it interacts with laser)
Fixed blocks should be handled separately so the solver won't try moving them.
Should have something like when [laser], [behavior] and describe how it bounces the ray?

Laser function that will travel until hitting something


Parser for the bff file --> translate the grid from bff into half-block steps so we have the grid and edges, designate which blocks are fixed and what spaces are available for blocks.

Solver - algorithm for finding block placement to light all of the P spots
Will want a class for laser, define how it interacts with blocks? Or object class can handle that. Maybe same person should do block classes and laser behavior, then the solver can work with laser 

Read board, define win condition, determine when win condition has been met; after that, call some function to process and print output with solution.


Will also need the  mechanics for placing/moving blocks and updating the laser reflection for different positioning of the blocks?

Output can be a bff file like what we had for input, or could be a png if we want to use PIL.


Unit tests? 

Something for solution output

This project is not a task that requires a GUI. We could but I don't know if there's a point.