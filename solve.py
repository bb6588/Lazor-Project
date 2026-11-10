from bffreader import puzzle_information
from solutionlogic import solve

puzzle = puzzle_information("mad_5.bff")
solution = solve(puzzle)

if solution is None:
    print("No solution found.")
else:
    print("Solution:", solution)