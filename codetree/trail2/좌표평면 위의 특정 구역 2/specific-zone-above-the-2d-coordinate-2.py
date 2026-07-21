n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

answer = float('inf')
for i in range(n):
    x_candid = [x[ii] for ii in range(n) if ii != i]
    y_candid = [y[ii] for ii in range(n) if ii != i]
    minX, maxX = min(x_candid), max(x_candid)
    minY, maxY = min(y_candid), max(y_candid)

    answer = min(answer, (maxX - minX) * (maxY - minY))

print(answer)