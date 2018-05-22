
def check_solution(possible_solution, penguin_positions):
    occupied_positions = penguin_positions[:]

    for piece in possible_solution:
        for square in piece:
            if square in occupied_positions:
                return False
            occupied_positions.append(square)

    print("Solution:", occupied_positions)
    return True
