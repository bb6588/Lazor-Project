"""This script controls laser behavior for the puzzle."""
from blockclasses import make_block


def build_block_map(puzzle, placement):
    """Make a dictionary of all blocks mapping position and block type.
    Returns a dictionary of the form {(row, col): A/B/C}."""
    grid = puzzle['board']
    blocks = {}
    for symbol, row, col in puzzle['fixed_blocks']:
        blocks[(row, col)] = make_block(symbol, (row, col), fixed=True)
    for (row, col), symbol in placement.items():
        # error handling for block placements that aren't physically possible
        if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
            raise ValueError(f'Position {(row, col)} is outside the board')
        if (row, col) in blocks:
            raise ValueError(f'Position {(row, col)} already has a fixed block')
        if grid[row][col].lower() != 'o':
            raise ValueError(f'Position {(row, col)} is not an open cell')
        blocks[(row, col)] = make_block(symbol, (row, col))
    return blocks


def cell_ahead(x, y, vx, vy):
    """Find the cell the laser will enter next and whether it's
    crossing a vertical (x) or horizontal (y) edge."""
    if x % 2 == 0:  # (vertical edge)
        col = x // 2 if vx > 0 else x // 2 - 1
        return (y // 2, col), 'x'
    row = y // 2 if vy > 0 else y // 2 - 1  # (horizontal edge)
    return (row, x // 2), 'y'


def simulate(puzzle, placement):
    """Follow laser beam and record the points on grid it passes through

    Returns:
        points_hit:
            set of (x, y) half-cell coordinates visited by the laser
        candidate_cells:
            list of (row, col) cells that the laser enters, the solver
            will try placing blocks in these cells to redirect the laser
            until it hits all targets.
    """
    grid = puzzle['board']
    n_rows, n_cols = len(grid), len(grid[0])
    blocks = build_block_map(puzzle, placement)

    points_hit = set()
    candidate_cells = []
    seen_cells = set()
    seen_states = set()  # (x, y, vx, vy), for loop detection

    stack = [(x, y, vx, vy)
             for (x, y), (vx, vy) in zip(puzzle['starting_positions'],
                                         puzzle['initial_direction'])]

    while stack:
        x, y, vx, vy = stack.pop()
        while (x, y, vx, vy) not in seen_states:
            seen_states.add((x, y, vx, vy))
            points_hit.add((x, y))

            cell, axis = cell_ahead(x, y, vx, vy)
            row, col = cell
            if not (0 <= row < n_rows and 0 <= col < n_cols):
                break  # ray left the grid

            block = blocks.get(cell)
            if block is None:
                if grid[row][col].lower() == 'o' and cell not in seen_cells:
                    seen_cells.add(cell)
                    candidate_cells.append(cell)
                x, y = x + vx, y + vy
                continue

            # Hit a block: it decides what comes out.
            for dx, dy in block.interact((vx, vy), axis):
                if (dx, dy) == (vx, vy):  # transmitted: enters the block
                    stack.append((x + vx, y + vy, dx, dy))
                else:  # reflected: stays on this edge point
                    stack.append((x, y, dx, dy))
            break

    return points_hit, candidate_cells


def check_win(puzzle, points_hit):
    """Check whether we hit all the targets. If all targets in the
    puzzle are contained in points_hit, will return true.
    """
    return all(p in points_hit for p in puzzle['target_points'])
