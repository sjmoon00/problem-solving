n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
colored = set()
for x, y in points:
    colored.add((x, y))
    cnt = 0
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if not(1 <= nx <= n) or not(1 <= ny <= n):
            continue
        if (nx, ny) in colored:
            cnt += 1
    
    if cnt == 3:
        print(1)
    else:
        print(0)