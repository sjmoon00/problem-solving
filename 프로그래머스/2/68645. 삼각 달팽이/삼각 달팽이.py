def solution(n):
    answer = []
    triangle = [[0] * i for i in range(1, n+1)]

    dirs = [(1, 0), (0, 1), (-1, -1)]
    pos = (-1, 0)
    dir_idx = 0
    cnt = 0
    for go in range(n, 0, -1):
        dir_x, dir_y = dirs[dir_idx]
        for _ in range(go):
            x, y = pos
            triangle[x][y] = cnt
            cnt += 1
            pos = (x + dir_x, y + dir_y)
        dir_idx = (dir_idx + 1) % 3
    triangle[pos[0]][pos[1]] = cnt
    
    for tri in triangle:
        answer += tri
    return answer