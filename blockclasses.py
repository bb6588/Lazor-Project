"Define block classes for solver"

def reflect(direction, axis):
    """Reflect across the x or y axis.

    if axis == 'x', the laser hit a vertical edge, so reflect x component
    if axis == 'y', the laser hit a horizontal edge, so reflect y component"""
    vx, vy = direction
    if axis == 'x':
        return (-vx, vy)
    else:
        return (vx, -vy)

class Block:
    """Define a generic block on the board.
    
    Parameters:
        position: 
            (row, column) of the block's location
        fixed:
            True if the block fixed/cannot be moved.
        """
    symbol = None

    def __init__(self, position, fixed=False):
        self.position = position
        self.fixed = fixed

    def interact(self, direction, axis):
        """Return the new direction of the laser after hitting the block.
        """

    def __repr__(self):
        kind = 'fixed' if self.fixed else 'movable'
        return f'{type(self).__name__}({self.position}, {kind})'

class ReflectBlock(Block):
    """Reflect block: reflects the laser across an axis"""
    symbol = 'A'
    def interact(self, direction, axis):
        return [reflect(direction, axis)]

class OpaqueBlock(Block):
    """Opaque block: absorbs the laser"""
    symbol = 'B'
    def interact(self, direction, axis):
        return []

class GlassBlock(Block):
    """Glass block: lets the laser pass through, but also reflects it;
    returns two lasers"""
    symbol = 'C'
    def interact(self, direction, axis):
        return [reflect(direction, axis), direction]

BLOCK_TYPES = {'A': ReflectBlock, 'B': OpaqueBlock, 'C': GlassBlock}

def make_block(symbol, position, fixed=False):
    """Translates .bff symbol (A, B, C) into a block object."""
    if symbol not in BLOCK_TYPES:
        raise ValueError(f'Unknown symbol {symbol} in board file')
    return BLOCK_TYPES[symbol](position, fixed)