board = [list(map(int, input().split())) for _ in range(19)]

def main():
    dxy = [(0, -1), (-1, -1), (-1, 0)]
    for i in range(19):
        for j in range(19):
            x, y = i, j
            stone = board[x][y]
            if stone == 0:
                continue

            for dx, dy in dxy:
                cnt = 1
                while board[x][y] == stone:
                    nx, ny = x + dx, y + dy
                    if not(0 <= nx < 19) or not(0 <= ny < 19):
                        break
                    n_stone = board[nx][ny]
                    if n_stone != stone:
                        break
                    x, y = nx, ny
                    cnt += 1
                if cnt == 5:
                    print(stone)
                    print((i + x) // 2 + 1, (j + y) // 2 + 1)
                    return True
    return False

if not main():
    print(0)