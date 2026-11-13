def save_solution(puzzle, solution, filename):
    """
    Saves the solved board to a text file.

    Parameters
    ----------
    puzzle : dict
        Dictionary containing the original board information.
    solution : dict
        Dictionary containing the positions and types of placed blocks.
    filename : str
        Name or path of the output text file.

    Returns
    -------
    None
        The solved board is saved to the output file.
    """
    if solution is None:
        raise ValueError('No solution to save.')

    completed_board = []

    # Create a copy of the original board
    for row in puzzle['board']:
        new_row = []
        for square in row:
            new_row.append(square)
        completed_board.append(new_row)

    # Place the movable blocks at the positions found by the solver
    for position in solution:
        row = position[0]
        column = position[1]
        block_type = solution[position]
        completed_board[row][column] = block_type

    output_file = open(filename, 'w')
    output_file.write('GRID START\n')

    for row in completed_board:
        row_text = ' '.join(row)
        output_file.write(row_text + '\n')

    output_file.write('GRID STOP\n')

    # Explanation of symbols used in the output file
    output_file.write('\nKEY:\n')
    output_file.write('A: Reflective block\n')
    output_file.write('B: Opaque block\n')
    output_file.write('C: Refractive block\n')
    output_file.write('o: Empty square where a moveable block can be placed\n')
    output_file.write('x: Unavailable square where a block cannot be placed\n')

    output_file.write('\nINSTRUCTIONS:\n')
    output_file.write('Use the grid above as a guide to solve the puzzle.\n')
    output_file.write('Place each movable block in the position shown on the grid.\n')
    output_file.write('Leave any fixed blocks in their original positions.\n')
    output_file.write('Refer to the key above to identify each block type.\n')

    output_file.close()

