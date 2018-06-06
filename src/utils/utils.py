import src.utils.positions as positions


def print_solution(solution, penguins):
    """
    Prints the solution. A different letter for each piece type and P for penguins.
    """
    row = 0
    while row < positions.board_size[1]:
        col = 0
        text_row = "   {}     {}".format(_text_for_position(col + 1, row, solution, penguins),
                                         _text_for_position(col + 3, row, solution, penguins))
        print(text_row)
        text_row = "{}     {}     {}".format(_text_for_position(col, row, solution, penguins),
                                             _text_for_position(col + 2, row, solution, penguins),
                                             _text_for_position(col + 4, row, solution, penguins))
        print(text_row)

        row += 1


def _text_for_position(col, row, solution, penguins):
    """
    Given col and row and the solution returns a letter for the piece,
    P for penguins and " " for possible blank squares (some challenges
    have 2 or 3 penguins instead of 4)
    """
    allocated_piece = None

    position = (col, row)

    if position in penguins:
        return "P"

    for piece in solution:
        # for a solution, a (col, row) exists only for one piece
        if position in piece:
            allocated_piece = piece

    if allocated_piece is None:
        return " "

    for name in positions.all_dictionary.keys():
        if allocated_piece in positions.all_dictionary[name]:
            return name

    raise Exception("Piece not in the piece list?")


if __name__ == "__main__":
    print_solution([], [(1,1), (2,0), (2,3), (3,1)])
