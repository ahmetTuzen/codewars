def valid_solution(board):
    # get rows columns and squares
    total = []
    for i in range(9):
        total.append(board[i])

    for i in range(3):
        for j in range(3):
            square = []
            for part in board[i*3:(i+1)*3]:
                square += part[j*3:(j+1)*3]
            total.append(square)

    for i in range(9):
        col = []
        for j in range(9):
            col.append(board[j][i])
        total.append(col)

    # validation

    for part in total:
        if len(set(part)) != 9:
            return False

    return True
