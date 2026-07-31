N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

low = min(x[0] for x in ranges)
high = max(x[1] for x in ranges)
answer = max(0, C*N, H*N)
for t in range(low, high + 1):
    output = 0
    for l, h in ranges:
        if t < l:
            output += C
        elif l <= t <= h:
            output += G
        elif t > h:
            output += H
    answer = max(answer, output)

print(answer)