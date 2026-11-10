def bff_reader(filename):
    """
    Reads a .bff file and removes unnecessary lines.

    Parameters
    ----------
    filename : str
        Name or path of the .bff file.

    Returns
    -------
    data_only : list of str
        Lines without comments, blank lines, or extra whitespace.
    """
    bff = open(filename, 'r')
    text = bff.readlines()
    bff.close()

    data_only = []

    # Remove blank lines, comments, #, extra whitespace
    for line in text:
        line = line.strip()

        if line != '':
            if '#' not in line:
                data_only.append(line)

    if len(data_only) == 0:
        raise ValueError('The .bff file is empty.')

    return data_only


def read_grid(data_only):
    """
    Reads the grid and converts it into a 2D list.

    Parameters
    ----------
    data_only : list of str
        Lines from the .bff file without unnecessary information.

    Returns
    -------
    board_representation : list of lists
        2D list containing the symbols for each square in the grid.
    """
    filtered_grid = []
    part_of_grid = False

    # Find the start and end of the grid and collect the rows between them
    for line in data_only:
        marker = line.strip().casefold()

        if line == "grid start":
            part_of_grid = True
        elif line == 'grid stop':
            part_of_grid = False
        elif part_of_grid:
            filtered_grid.append(line)

    if len(filtered_grid) == 0:
        raise ValueError('No grid information found.')

    board_representation = []

    # Separate each row into individual squares
    for row in filtered_grid:
        rows = row.split()
        board_representation.append(rows)

    for row in board_representation:
        if len(row) != len(board_representation[0]):
            raise ValueError('Grid rows have different lengths.')

    return board_representation


def fixed_block_locations(board_representation):
    """
    Identifies fixed blocks and their positions in the grid.

    Parameters
    ----------
    board_representation : list of lists
        2D list containing the symbols for each square in the grid.

    Returns
    -------
    fixed_blocks : list of tuples
        Block type, row, and column of each fixed block.
    """
    fixed_blocks = []

    for row in range(len(board_representation)):
        for column in range(len(board_representation[row])):
            block = board_representation[row][column]

            if block == 'A' or block == 'B' or block == 'C':
                fixed_blocks.append((block, row, column))

    return fixed_blocks


def moveable_block_quantities(data_only):
    """
    Determines the number of moveable blocks of each type.

    Parameters
    ----------
    data_only : list of str
        Lines from the .bff file without unnecessary information.

    Returns
    -------
    moveable_blocks : dict
        Dictionary containing the quantities of moveable reflective,
        opaque, and refractive blocks.
    """
    moveable_blocks = {'A': 0, 'B': 0, 'C': 0}
    specifies_moveable_block = False

    # Read movable block quantities between GRID STOP and the laser information
    for line in data_only:
        if line == 'GRID STOP':
            specifies_moveable_block = True

        elif line[0] == 'L':
            specifies_moveable_block = False

        elif specifies_moveable_block:
            block_type = line.split()[0]
            if block_type not in moveable_blocks:
                raise ValueError('Invalid moveable block type.')
            quantity = line.split()[1]
            quantity = int(quantity)
            moveable_blocks[block_type] = quantity

    return moveable_blocks


def lazor_information(data_only):
    """
    Finds the starting positions and initial directions of all lasers.

    Parameters
    ----------
    data_only : list of str
        Lines from the .bff file without unnecessary information.

    Returns
    -------
    starting_positions : list of tuples
        Starting (x, y) coordinates of each laser.

    initial_direction : list of tuples
        Initial (vx, vy) direction of each laser.
    """
    starting_positions = []
    initial_direction = []

    for line in data_only:
        if line[0] == 'L':
            values = line.split()
            if len(values) != 5:
                raise ValueError('Invalid laser information.')

            x = int(values[1])
            y = int(values[2])
            starting_position = (x, y)
            starting_positions.append(starting_position)

            vx = int(values[3])
            vy = int(values[4])
            direction = (vx, vy)
            initial_direction.append(direction)

    if len(starting_positions) == 0:
        raise ValueError('No lasers found.')

    return starting_positions, initial_direction


def target_points(data_only):
    """
    Finds the coordinates of all target points in the puzzle.

    Parameters
    ----------
    data_only : list of str
        Lines from the .bff file without unnecessary information.

    Returns
    -------
    points_to_intersect : list of tuples
        (x, y) coordinates of the target points that lasers must hit.
    """
    points_to_intersect = []

    # Target Points indicated in file by starting with letter 'P'
    for line in data_only:
        if line[0] == 'P':
            values = line.split()
            if len(values) != 3:
                raise ValueError('Invalid target point information.')

            # x and y coordinates lie in indices 1 and 2
            x = int(values[1])
            y = int(values[2])
            point = (x, y)
            points_to_intersect.append(point)
    if len(points_to_intersect) == 0:
        raise ValueError('No target points found.')
    return points_to_intersect


def puzzle_information(filename):
    """
    Collects all puzzle information from a .bff file into a dictionary.

    Parameters
    ----------
    filename : str
        Name or path of the .bff file.

    Returns
    -------
    puzzle : dict
        Dictionary containing the board, fixed blocks, moveable
        blocks, laser positions, laser directions, and target points.
    """
    data_only = bff_reader(filename)

    board_representation = read_grid(data_only)
    fixed_blocks = fixed_block_locations(board_representation)
    moveable_blocks = moveable_block_quantities(data_only)
    starting_positions, initial_direction = lazor_information(data_only)
    points_to_intersect = target_points(data_only)

    puzzle = {
        'board': board_representation,
        'fixed_blocks': fixed_blocks,
        'moveable_blocks': moveable_blocks,
        'starting_positions': starting_positions,
        'initial_direction': initial_direction,
        'target_points': points_to_intersect
    }
    return puzzle