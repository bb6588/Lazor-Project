"""The solver for the Lazor puzzle. To use, open the project file in terminal and run command:
python solve.py <[your puzzle].bff>
If a solution is found, this script will output a text file, [your puzzle]_solution.txt, with
a diagram of the solution. 
If there is no solution, you'll see a printout in terminal saying so. 
"""

import os
import sys 
from bffreader import puzzle_information
from solutionlogic import solve
from output import save_solution

# Error handling for if no board file is specified to solve
if len(sys.argv) < 2:
    print("No board file specified. Use command: python solve.py <board.bff>")
    sys.exit(1)

# Error handling for if there's no board with the name given
if not os.path.exists(sys.argv[1]):
    print("Could not find file. Please confirm the bff exists in this directory.")
    sys.exit(1)

# Get basename for output file from the name of command line input file
input_file = sys.argv[1]
base_name = os.path.splitext(os.path.basename(input_file))[0]
output_file = base_name + "_solution.txt"

# Pass puzzle info from bffreader into solver
puzzle = puzzle_information(input_file)
solution = solve(puzzle)

if solution is None:
    print("No solution found.")
else:
    print("Solution:", solution)
    save_solution(puzzle, solution, output_file)
    print("For diagram, see", output_file)