"""Depth-first solver for the Lazor puzzle.
Process is:
1. Place a block in one of the available cells that the laser crosses.
2. Simulate laser paths and check win condition (all targets hit)
3. If not a win, recursively test placing another block in one of the 
available cells (including the cells that the first block placement made available).
4. If a solution isn't found down that path, backtrack and try a different initial cell or block type.
5. Repeat until solution found (or until we confirm no solutions exist)
"""
from laser import simulate, check_win





def solve(puzzle):
    """Find a placement of the movable blocks that hits every target.

    Returns
    -------
    dict or None
        {(row, col): 'A'/'B'/'C'} for every block moved for the solution, or None if
        no solution exists.
    """
    remaining = dict(puzzle['moveable_blocks'])
    visited = set()  # placements already explored, order-independent
    return _search(puzzle, {}, remaining, visited)


def _search(puzzle, placement, remaining, visited):
    """Recursive step: Check lasers, test block placement, and recurse if necessary."""
    # Using frozenset to store placements we've already explored; won't consider placing 
    # the same blocks in a different order as a new placement.
    key = frozenset(placement.items())
    if key in visited:
        return None
    visited.add(key)
    
    # Try reflect blocks first, then glass blocks, then opaque blocks
    TRY_ORDER = ('A', 'C', 'B')

    points_hit, candidates = simulate(puzzle, placement)

    # If we win, return solution block placement
    if check_win(puzzle, points_hit):
        return dict(placement)

    # If we can't place any more blocks, return None
    if sum(remaining.values()) == 0:
        return None

    # Placement loop: try placing a block in each available cell, backtrack if no solution
    for cell in candidates:
        for symbol in TRY_ORDER: # will cycle through all reflect blocks first, then glass, then opaque
            if remaining.get(symbol, 0) == 0: # run out of current block type
                continue # move on to next block type

            placement[cell] = symbol
            remaining[symbol] -= 1

            result = _search(puzzle, placement, remaining, visited)
            if result is not None:
                return result

            # Backtrack.
            remaining[symbol] += 1
            del placement[cell]

    return None
