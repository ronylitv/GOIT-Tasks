def done_or_not(board: list):
    for i in board:
        p = sorted(i)
        if p != [l for l in range(1, 10)]:
            return 'Try again!'

    pos = 0
    while True:
        try:
            board[pos][:pos+3]
    return 'Finished!'

print(done_or_not([
    [1, 3, 2, 5, 7, 9, 4, 6, 8],
    [4, 9, 8, 2, 6, 1, 3, 7, 5],
    [7, 5, 6, 3, 8, 4, 2, 1, 9],
    [6, 4, 3, 1, 5, 8, 7, 9, 2],
    [5, 2, 1, 7, 9, 3, 8, 4, 6],
    [9, 8, 7, 4, 2, 6, 5, 3, 1],
    [2, 1, 4, 9, 3, 5, 6, 8, 7],
    [3, 6, 5, 8, 1, 7, 9, 2, 4],
    [8, 7, 9, 6, 4, 2, 1, 5, 3]]))