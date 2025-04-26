def solution(keyinput, board):
    dic = {
        'left': (-1, 0),
        'right': (1, 0),
        'up': (0, 1),
        'down': (0, -1)
    }
    x_limit = board[0] // 2
    y_limit = board[1] // 2
    pos = (0, 0)
    for key in keyinput:
        d = dic[key] 
        nx, ny = pos[0] + d[0], pos[1] + d[1]
        if not(-x_limit <= nx <= x_limit) or not(-y_limit <= ny <= y_limit):
            continue

        pos = (nx, ny)
    return pos