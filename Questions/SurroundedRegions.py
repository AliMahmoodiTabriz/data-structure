
def solve(board: list[list[str]]):
    for i in range(1, len(board)-1):
        for j in range(1, len(board[0])-1):
            if board[i][j] != "X":
                path = {}
                if not move(path, board, i, j):
                    for item in path.items():
                        board[item[1][0]][item[1][1]] = "X"


def move(path, board, i, j):
    if i == 0 or j == 0 or i == len(board)-1 or j == len(board[0])-1:
        return True
    key = str(i)+str(j)
    if key not in path:
        path[key] = [i, j]
    else:
        return False

    left = board[i][j-1]
    right = board[i][j+1]
    up = board[i-1][j]
    down = board[i+1][j]

    if left == "O":
        if move(path, board, i, j-1):
            return True

    if right == "O":
        if move(path, board, i, j+1):
            return True

    if up == "O":
        if move(path, board, i-1, j):
            return True

    if down == "O":
        if move(path, board, i+1, j):
            return True

    return False


board = [["X", "X", "X", "X"],
         ["X", "O", "O", "X"],
         ["X", "X", "O", "X"],
         ["X", "O", "X", "X"]]

board = [["X", "O", "X", "O", "X", "O"],
         ["O", "X", "O", "X", "O", "X"],
         ["X", "O", "X", "O", "X", "O"],
         ["O", "X", "O", "X", "O", "X"]]

board = [
        ["O", "X", "X", "O", "X"],
        ["X", "O", "O", "X", "O"],
        ["X", "O", "X", "O", "X"],
        ["O", "X", "O", "O", "O"],
        ["X", "X", "O", "X", "O"]
]
solve(board)
print(board)
