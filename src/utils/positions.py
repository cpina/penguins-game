# See README.md to understand the game.
#
# The first challenge that we found was to know
# which possible positions the pieces could be put
# in the board.
#
# Given that the board is quite small and the pieces
# quite irregular we opted for listing all the positions
# that the pieces could be in.
#
# Feel free to not use this and generate them programatically!
#
# There are 4 pieces named L, C, Z and R
# (based on the "shape" of the pieces).
# The board is not a square board: it has a bit of an
# irregular shape. This made things a bit more difficult.

# See the image:
# The penguins are in this positions (following the same
# position-scheme as the pieces here):
#
# [(0,0), (1,2), (2,3), (3,1)]
# So, the format is: (column, row), zero-indexed, count the number
# of empty ice-blocks from the top-left to the position.
#
# In the same ...
# The piece is in the position: [(0, 1), (0, 2), (1, 1), (2, 1)]
# A representation of the board using public_utils.print_solution:
#
#    Z     Z
# P     Z     Z
#    C     P
# C     C     R
#    P     R
# C     L     R
#    L     L
# L     P     R

L = [
    [(0,0), (0,1), (0,2), (1,0)],
    [(0,1), (0,2), (0,3), (1,1)],
    [(1,1), (1,2), (1,3), (2,0)],
    [(2,0), (2,1), (2,2), (3,0)],
    [(2,1), (2,2), (2,3), (3,1)],
    [(3,1), (3,2), (3,3), (4,0)],
    [(0,1), (1,1), (2,0), (3,1)],
    [(1,1), (2,0), (3,0), (4,0)],
    [(0,2), (1,2), (2,1), (3,2)],
    [(1,2), (2,1), (3,1), (4,1)],
    [(0,3), (1,3), (2,2), (3,3)],
    [(1,3), (2,2), (3,2), (4,2)],
    [(0,1), (1,2), (2,2), (2,3)],
    [(0,0), (1,1), (2,1), (2,2)],
    [(1,1), (2,1), (3,2), (3,3)],
    [(2,1), (3,2), (4,2), (4,3)],
    [(1,0), (2,0), (3,1), (3,2)],
    [(2,0), (3,1), (4,1), (4,2)],
    [(0,2), (1,0), (1,1), (1,2)],
    [(0,3), (1,1), (1,2), (1,3)],
    [(1,3), (2,0), (2,1), (2,2)],
    [(2,2), (3,0), (3,1), (3,2)],
    [(2,3), (3,1), (3,2), (3,3)],
    [(3,3), (4,0), (4,1), (4,2)],
    [(0,0), (1,1), (2,0), (3,0)],
    [(0,1), (1,2), (2,1), (3,1)],
    [(1,1), (2,1), (3,1), (4,0)],
    [(0,2), (1,3), (2,2), (3,2)],
    [(1,2), (2,2), (3,2), (4,1)],
    [(1,3), (2,3), (3,3), (4,2)],
    [(0,0), (0,1), (1,2), (2,2)],
    [(0,1), (0,2), (1,3), (2,3)],
    [(1,0), (1,1), (2,1), (3,2)],
    [(1,1), (1,2), (2,2), (3,3)],
    [(2,0), (2,1), (3,2), (4,2)],
    [(2,1), (2,2), (3,3), (4,3)],
]

C = [
    [(0,0), (0,1), (1,0), (1,2)],
    [(0,1), (0,2), (1,1), (1,3)],
    [(1,1), (1,2), (2,0), (2,2)],
    [(1,2), (1,3), (2,1), (2,3)],
    [(2,0), (2,1), (3,0), (3,2)],
    [(2,1), (2,2), (3,1), (3,3)],
    [(3,1), (3,2), (4,0), (4,2)],
    [(0,0), (0,1), (1,0), (2,0)],
    [(0,1), (0,2), (1,1), (2,1)],
    [(0,2), (0,3), (1,2), (2,2)],
    [(1,1), (1,2), (2,0), (3,1)],
    [(1,2), (1,3), (2,1), (3,2)],
    [(2,0), (2,1), (3,0), (4,0)],
    [(2,1), (2,2), (3,1), (4,1)],
    [(2,2), (2,3), (3,2), (4,2)],
    [(0,0), (1,0), (2,0), (2,1)],
    [(0,1), (1,1), (2,1), (2,2)],
    [(0,2), (1,2), (2,2), (2,3)],
    [(1,1), (2,0), (3,1), (3,2)],
    [(1,2), (2,1), (3,2), (3,3)],
    [(2,0), (3,0), (4,0), (4,1)],
    [(2,1), (3,1), (4,1), (4,2)],
    [(2,2), (3,2), (4,2), (4,3)],
    [(0,0), (0,2), (1,1), (1,2)],
    [(0,1), (0,3), (1,2), (1,3)],
    [(1,0), (1,2), (2,0), (2,1)],
    [(1,1), (1,3), (2,1), (2,2)],
    [(2,0), (2,2), (3,1), (3,2)],
    [(2,1), (2,3), (3,2), (3,3)],
    [(3,0), (3,2), (4,0), (4,1)],
    [(3,1), (3,3), (4,1), (4,2)],
    [(0,1), (1,2), (2,0), (2,1)],
    [(0,2), (1,3), (2,1), (2,2)],
    [(1,1), (2,1), (3,0), (3,1)],
    [(1,2), (2,2), (3,1), (3,2)],
    [(1,3), (2,3), (3,2), (3,3)],
    [(2,1), (3,2), (4,0), (4,1)],
    [(2,2), (3,3), (4,1), (4,2)],
    [(0,0), (0,1), (1,2), (2,1)],
    [(0,1), (0,2), (1,3), (2,2)],
    [(1,0), (1,1), (2,1), (3,1)],
    [(1,1), (1,2), (2,2), (3,2)],
    [(1,2), (1,3), (2,3), (3,3)],
    [(2,0), (2,1), (3,2), (4,1)],
    [(2,1), (2,2), (3,3), (4,2)],
    ]

Z = [
    [(0,0), (0,1), (1,2), (1,3)],
    [(1,0), (1,1), (2,1), (2,2)],
    [(1,1), (1,2), (2,2), (2,3)],
    [(2,0), (2,1), (3,2), (3,3)],
    [(3,0), (3,1), (4,1), (4,2)],
    [(3,1), (3,2), (4,2), (4,3)],
    [(0,2), (1,1), (1,2), (2,0)],
    [(0,3), (1,2), (1,3), (2,1)],
    [(1,2), (2,0), (2,1), (3,0)],
    [(1,3), (2,1), (2,2), (3,1)],
    [(2,2), (3,1), (3,2), (4,0)],
    [(2,3), (3,2), (3,3), (4,1)],
    [(0,0), (1,1), (2,0), (3,1)],
    [(0,1), (1,2), (2,1), (3,2)],
    [(0,2), (1,3), (2,2), (3,3)],
    [(1,0), (2,0), (3,0), (4,0)],
    [(1,1), (2,1), (3,1), (4,1)],
    [(1,2), (2,2), (3,2), (4,2)],
    [(1,3), (2,3), (3,3), (4,3)],
    ]

R = [
    [(0,0), (0,1), (0,2), (1,2)],
    [(0,1), (0,2), (0,3), (1,3)],
    [(1,0), (1,1), (1,2), (2,1)],
    [(1,1), (1,2), (1,3), (2,2)],
    [(2,0), (2,1), (2,2), (3,2)],
    [(2,1), (2,2), (2,3), (3,3)],
    [(3,0), (3,1), (3,2), (4,1)],
    [(3,1), (3,2), (3,3), (4,2)],
    [(0,1), (1,1), (1,2), (2,0)],
    [(0,2), (1,2), (1,3), (2,1)],
    [(1,1), (2,0), (2,1), (3,0)],
    [(1,2), (2,1), (2,2), (3,1)],
    [(1,3), (2,2), (2,3), (3,2)],
    [(2,1), (3,1), (3,2), (4,0)],
    [(2,2), (3,2), (3,3), (4,1)],
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,1), (0,2), (1,2), (2,2)],
    [(0,2), (0,3), (1,3), (2,3)],
    [(1,0), (1,1), (2,0), (3,1)],
    [(1,1), (1,2), (2,1), (3,2)],
    [(1,2), (1,3), (2,2), (3,3)],
    [(2,0), (2,1), (3,1), (4,1)],
    [(2,1), (2,2), (3,2), (4,2)],
    [(2,2), (2,3), (3,3), (4,3)],
    [(0,0), (1,0), (1,1), (1,2)],
    [(0,1), (1,1), (1,2), (1,3)],
    [(1,1), (2,0), (2,1), (2,2)],
    [(1,2), (2,1), (2,2), (2,3)],
    [(2,0), (3,0), (3,1), (3,2)],
    [(2,1), (3,1), (3,2), (3,3)],
    [(3,1), (4,0), (4,1), (4,2)],
    [(3,2), (4,1), (4,2), (4,3)],
    [(0,1), (1,0), (1,1), (2,0)],
    [(0,2), (1,1), (1,2), (2,1)],
    [(0,3), (1,2), (1,3), (2,2)],
    [(1,2), (2,0), (2,1), (3,1)],
    [(1,3), (2,1), (2,2), (3,2)],
    [(2,1), (3,0), (3,1), (4,0)],
    [(2,2), (3,1), (3,2), (4,1)],
    [(2,3), (3,2), (3,3), (4,2)],
    [(0,0), (1,1), (2,0), (2,1)],
    [(0,1), (1,2), (2,1), (2,2)],
    [(0,2), (1,3), (2,2), (2,3)],
    [(1,0), (2,0), (3,0), (3,1)],
    [(1,1), (2,1), (3,1), (3,2)],
    [(1,2), (2,2), (3,2), (3,3)],
    [(2,0), (3,1), (4,0), (4,1)],
    [(2,1), (3,2), (4,1), (4,2)],
    [(2,2), (3,3), (4,2), (4,3)],
]

all = [L, C, Z, R]

all_dictionary = {'L': L,
                  'C': C,
                  'Z': Z,
                  'R': R
                  }

board_size = (5,4)