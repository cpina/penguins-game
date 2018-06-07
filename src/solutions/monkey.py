
import random

import sys
import os
sys.path.append((os.path.join(sys.path[0], "../..")))
sys.path.append("../../..")

import src.utils.positions as positions
import src.solutions.solutions_utils as solution_utils

"""
Attempts to solve the puzzle with random positions. It doesn't finish in minutes.
"""


def resolve(penguin_positions):
    solved = False
    combination_counter = 0

    while not solved:
        possible_solution = random.choice(positions.L) + random.choice(positions.C) + random.choice(positions.Z) + random.choice(positions.R)
        combination_counter += 1

        if solution_utils.check_solution(possible_solution, penguin_positions):
            print("SOLUTION FOUND:", possible_solution)
            solved = True

        if combination_counter % 100000 == 0:
            print("Tested:", combination_counter)

    print("combination counter:", combination_counter)

if __name__ == "__main__":
    #penguin_positions = []
    #penguin_positions = [(1,1), (2,0), (2,3), (3,1)] # easy
    #penguin_positions = [(2,0), (2,2)] # master
    penguin_positions = [(0, 0), (1, 2), (2, 3), (3, 1)]  # junior
    resolve(penguin_positions)


