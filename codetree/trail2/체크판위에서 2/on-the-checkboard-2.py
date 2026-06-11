R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

patterns = set(['WBWB', 'BWBW'])
answer = 0
for i in range(1, R - 2):
    for j in range(1, C - 2):
        for k in range(i + 1, R - 1):
            for l in range(j + 1, C - 1):
                start, end = grid[0][0], grid[R - 1][C - 1]
                mid1, mid2 = grid[i][j], grid[k][l]
                if start + mid1 + mid2 + end in patterns:
                    answer += 1

print(answer)