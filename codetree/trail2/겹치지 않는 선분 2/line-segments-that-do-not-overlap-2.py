n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort()

overlapped = [False] * n
for i in range(n):
    a1, a2 = lines[i][0], lines[i][1]
    for j in range(i):
        b1, b2 = lines[j][0], lines[j][1]

        if b2 >= a2:
            overlapped[j] = True
            overlapped[i] = True

print(n - sum(overlapped))