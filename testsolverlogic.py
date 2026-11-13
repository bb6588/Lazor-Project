"""Test the solver by making sure it works on the example.
This maybe doesn't need to exist. I guess the distinction is we know 100% the example is solvable and should have an output.
"""

from bffreader import puzzle_information
from laser import check_win, simulate
from solutionlogic import solve

# Check solver works.
if __name__ == "__main__":
    puzzle = puzzle_information("example.bff")
    placement = solve(puzzle)
    points_hit, _ = simulate(puzzle, placement)
    if check_win(puzzle, points_hit):
        print("Solver works.")
    else:
        print("Solver does not work. Check git log and maybe revert to an older version.")
