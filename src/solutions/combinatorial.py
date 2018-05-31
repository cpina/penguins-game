
import itertools
import src.utils.positions as positions
import src.utils.utils as utils
import src.solutions.solutions_utils as solutions_utils

"""
Tries all the possible combinations: a pure product of all the possible pieces-positions.

Easy to implement, it takes a few seconds in a normal computer.
"""


def resolve(penguin_positions):
    solution_counter = 0
    combination_counter = 0
    solution = None
    for possible_solution in itertools.product(*positions.all):
        combination_counter += 1
        if solutions_utils.check_solution(possible_solution, penguin_positions):
            print("SOLUTION FOUND:", possible_solution)
            solution_counter += 1
            solution = possible_solution
            break

    print("solution counter:", solution_counter)
    print("combination counter:", combination_counter)

    return solution

if __name__ == "__main__":
    #penguin_positions = []
    #penguin_positions = [(1,1), (2,0), (2,3), (3,1)] # easy
    #penguin_positions = [(2,0), (2,2)] # master
    #penguin_positions = [(0, 0), (1, 2), (2, 3), (3, 1)]  # junior
    penguin_positions = [(0,0), (1,2), (2,3), (3,1)]
    solution = resolve(penguin_positions)
    utils.print_solution(solution, penguin_positions)

