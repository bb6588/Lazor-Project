"""Test for the laser, check that it is bouncing off blocks as intended and that the win condition is being checked correctly. This test will print out the points hit by the laser and whether or not the win condition is met."
"""

from laser import simulate, check_win

puzzle = {
    'board': [['o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o'],
              ['o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o']],
    'fixed_blocks': [],
    'moveable_blocks': {},
    'starting_positions': [(0, 1)],
    'initial_direction': [(1, 1)],
    'target_points': [(3, 4)],
}

# If we have no blocks, the laser should not hit the target
hit, _ = simulate(puzzle, {})
if check_win(puzzle, hit):
    print("Laser works if board is empty.")
else:
    print("Laser does not work properly on empty board.")

# Place an opaque block, make sure it blocks the laser (check_win should
# return False)
hit, _ = simulate(puzzle, {(0, 0): 'B'})
if not check_win(puzzle, hit):
    print('Laser works on opaque block.')
else:
    print("Laser doesn't work properly on opaque blocks.")

# Place a reflect block, make sure it bounces and hits target.
hit, _ = simulate(puzzle, {(0, 0): 'A'})
if not check_win(puzzle, hit):
    print("Laser works on reflect block.")
else:
    print("Laser doesn't work properly on reflect blocks.")

# Place a glass block, make sure it allows the laser to pass through and
# hit target.
hit, _ = simulate(puzzle, {(0, 0): 'C'})
if check_win(puzzle, hit):
    print("Laser works on glass block.")
else:
    print("Something's up with the laser, misbehaving with glass blocks.")
