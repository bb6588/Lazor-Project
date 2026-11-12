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
    output_file.close()

