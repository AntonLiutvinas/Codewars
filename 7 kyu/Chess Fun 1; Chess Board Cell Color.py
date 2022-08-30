def chess_board_cell_color(cell1, cell2):
    sum1 = 0
    sum2 = 0
    letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    numbers = list(range(8))
    dictionary = {key:value for key, value in zip(letters, numbers)}
    for i in cell1:
        try:
            sum1 += dictionary.get(i)
        except TypeError:
            sum1 += int(i)
    for i in cell2:
        try:
            sum2 += dictionary.get(i)
        except TypeError:
            sum2 += int(i)
    return True if sum1 % 2 == sum2 % 2 else False
print(chess_board_cell_color("A1", "C2"))