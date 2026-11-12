from bffreader import puzzle_information
from solutionlogic import solve
from output import save_solution

puzzle = puzzle_information("mad_5.bff")
solution = solve(puzzle)

if solution is None:
    print("No solution found.")
else:
    print("Solution:", solution)
    save_solution(puzzle, solution, 'mad_5_solution.txt')