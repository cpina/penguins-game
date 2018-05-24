import constraint
import positions
import utils

def resolve(penguin_positions):
    problem = constraint.Problem(constraint.RecursiveBacktrackingSolver())
    problem.addVariable("L", positions.L)
    problem.addVariable("C", positions.C)
    problem.addVariable("Z", positions.Z)
    problem.addVariable("R", positions.R)

    problem.addConstraint(lambda L,C,Z,R: utils.check_solution([L,C,Z,R], penguin_positions))

    solutions = problem.getSolution()

    print(solutions)

if __name__ == "__main__":
    #penguin_positions = []
    #penguin_positions = [(1,1), (2,0), (2,3), (3,1)] # easy
    #penguin_positions = [(2,0), (2,2)] # master
    penguin_positions = [(0, 0), (1, 2), (2, 3), (3, 1)]  # junior
    resolve(penguin_positions)
