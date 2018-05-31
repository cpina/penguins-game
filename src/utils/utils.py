import src.utils.positions as positions


# L, C, Z, R
def text_for_position(col, row, solution, penguins):
    allocated_piece = None

    position = (col, row)

    if position in penguins:
        return "P"

    for piece in solution:
        # for a solution, a (col, row) exists only for one piece
        if position in piece:
            allocated_piece = piece

    if allocated_piece == None:
        return " "

    for name in positions.all_dictionary.keys():
        if allocated_piece in positions.all_dictionary[name]:
            return name

    raise Exception("Piece not in the piece list?")


def print_solution(solution, penguins):
    row = 0
    while row < positions.board_size[1]:
        col = 0
        text_row = "   {}     {}".format(text_for_position(col+1, row, solution, penguins),
                                    text_for_position(col+3, row, solution, penguins))
        print(text_row)
        text_row = "{}     {}     {}".format(text_for_position(col, row, solution, penguins),
                                        text_for_position(col+2, row, solution, penguins),
                                        text_for_position(col+4, row, solution, penguins))
        print(text_row)

        row += 1


def print_solution(solution, penguins):
    row = 0
    while row < positions.board_size[1]:
        col = 0
        text_row = "   {}     {}".format(text_for_position(col+1, row, solution, penguins),
                                    text_for_position(col+3, row, solution, penguins))
        print(text_row)
        text_row = "{}     {}     {}".format(text_for_position(col, row, solution, penguins),
                                        text_for_position(col+2, row, solution, penguins),
                                        text_for_position(col+4, row, solution, penguins))
        print(text_row)

        row += 1

if __name__ == "__main__":
    print_solution([], [(1,1), (2,0), (2,3), (3,1)])
