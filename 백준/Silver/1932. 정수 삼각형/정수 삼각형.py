N = int(input())
tri = []
for _ in range(N):
    row = list(map(int, input().split()))
    tri.append(row)

for i in range(1, N):
    row = tri[i]
    for j, x in enumerate(row):
        if j == 0:
            up_right = tri[i-1][j]
            tri[i][j] += up_right
            continue
        elif j == len(row)-1:
            up_left = tri[i-1][j-1]
            tri[i][j] += up_left
            continue
        
        up_left, up_right = tri[i-1][j-1], tri[i-1][j]
        tri[i][j] += max(up_left, up_right)

print(max(tri[-1]))