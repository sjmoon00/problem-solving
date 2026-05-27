n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

blocks = [0] * (n+1)

for a, b in commands:
    for i in range(a, b+1):
        blocks[i] += 1

print(max(blocks))