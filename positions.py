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
print("L:", len(L))
print("C:", len(C))
print("Z:", len(Z))
print("R:", len(R))

all_dictionary = {'L': L,
                  'C': C,
                  'Z': Z,
                  'R': R
                  }

board_size = (5,4)