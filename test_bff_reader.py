"""Test for bffreader.py. Will print symbols for available movable blocks and board layout, and
specify if there are fixed blocks/which blocks are fixed.
"""

from bffreader import puzzle_information
b = puzzle_information('example.bff')
print(b['moveable_blocks'])
if b['fixed_blocks']:
    print(b['fixed_blocks'])
else:
    print('No fixed blocks')
for row in b['board']:
    print(row)
