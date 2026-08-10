n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)

minX, maxX = min(a), max(b)
answer = 0
for x in range(minX, maxX + 1):
    xx = x
    for aa, bb in zip(a, b):
        xx *= 2
        if not(aa <= xx <= bb):
            break
    else:
        answer = x
        break

print(answer)