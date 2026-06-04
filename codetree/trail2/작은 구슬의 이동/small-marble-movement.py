n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

dxy = [(1, 0), (0, 1), (0, -1), (-1, 0)]
mapper = {'D': 0, 'R': 1, 'L': 2, 'U': 3}

i = mapper[d]
for _ in range(t):
    nx, ny = r + dxy[i][0], c + dxy[i][1]
    if not(1 <= nx <= n) or not(1 <= ny <= n):
        i = 3 - i
        continue
    
    r = nx
    c = ny

print(r, c)