from collections import defaultdict
N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

d = defaultdict(int)
for i in range(N):
    b1 = num[i]
    for j in range(max(0, i - K), min(N, i + K + 1)):
        if i == j: continue
        b2 = num[j]
        if b1 == b2:
            d[b1] += 1
            break

if not d:
    print(0)
else:
    t = sorted(d.items(), key= lambda x: (x[1], x[0]))
    print(t[-1][0])