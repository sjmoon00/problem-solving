import sys
import heapq as hq
input = sys.stdin.readline
N, M = map(int, input().split())
classes = []
for _ in range(N):
    t = list(map(int, input().split()))
    hq.heapify(t)
    classes.append(t)

answer = 1e9
max_value = 0
q = []

for i in range(N):
    value = hq.heappop(classes[i])
    hq.heappush(q, (value, i))
    max_value = max(max_value, value)

while True:
    value, i = hq.heappop(q)

    answer = min(answer, abs(value - max_value))

    if not classes[i]:
        break

    next_value = hq.heappop(classes[i])
    max_value = max(max_value, next_value)
    hq.heappush(q, (next_value, i))

print(answer)