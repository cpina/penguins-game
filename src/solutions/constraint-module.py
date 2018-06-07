import constraint

import sys
import os
sys.path.append((os.path.join(sys.path[0], "../..")))
sys.path.append("../../..")

import src.utils.positions as positions
import src.solutions.solutions_utils as solution_utils
import src.utils.utils as utils


def resolve(penguin_positions):
    problem = constraint.Problem(constraint.RecursiveBacktrackingSolver())
    problem.addVariable("L", positions.L)
    problem.addVariable("C", positions.C)
    problem.addVariable("Z", positions.Z)
    problem.addVariable("R", positions.R)

    problem.addConstraint(lambda L,C,Z,R: solution_utils.check_solution([L,C,Z,R], penguin_positions))

    solutions = problem.getSolution()

    print(solutions)

    # TODO: convert this solution format to the usual solutions
    utils.print_solution(solutions)

if __name__ == "__main__":
    #penguin_positions = []
    #penguin_positions = [(1,1), (2,0), (2,3), (3,1)] # easy
    #penguin_positions = [(2,0), (2,2)] # master
    penguin_positions = [(0, 0), (1, 2), (2, 3), (3, 1)]  # junior
    resolve(penguin_positions)
