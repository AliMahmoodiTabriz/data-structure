def judgeCircle(moves: str) -> bool:
    x = 0
    y = 0
    for move in moves:
        if move == 'U':
            y += 1
            continue
        if move == 'D':
            y -= 1
            continue
        if move == 'L':
            x -= 1
            continue
        if move == 'R':
            x += 1
            continue
    return x == 0 and y == 0

print(judgeCircle(['U','D','R','L']))
