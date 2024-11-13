
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

def solveBest(board: list[list[str]]):
    if not board or not board[0]:
        return
    
    rows, cols = len(board), len(board[0])

    # DFS kullanarak kenarlara ulaşan 'O' hücrelerini geçici olarak işaretle
    def mark_border_reachable(i, j):
        if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != 'O':
            return
        board[i][j] = 'T'  # Geçici işaretleme
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            mark_border_reachable(ni, nj)

    # Kenardaki 'O' hücrelerinden başla
    for i in range(rows):
        if board[i][0] == 'O':
            mark_border_reachable(i, 0)
        if board[i][cols - 1] == 'O':
            mark_border_reachable(i, cols - 1)
    for j in range(cols):
        if board[0][j] == 'O':
            mark_border_reachable(0, j)
        if board[rows - 1][j] == 'O':
            mark_border_reachable(rows - 1, j)

    # Tüm tahta üzerinde gez ve 'O' olanları 'X' yap, 'T' olanları ise geri 'O' yap
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'O':
                board[i][j] = 'X'  # Çevrili bölge
            elif board[i][j] == 'T':
                board[i][j] = 'O'  # Kenarlara bağlı olanları geri döndür

# Örnek kullanım
board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
solveBest(board)
print(board)  # Çıktı: [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]


