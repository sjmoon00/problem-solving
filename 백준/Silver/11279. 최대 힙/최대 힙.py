import heapq as hq
import sys
input = sys.stdin.readline
N = int(input())
max_heap = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if max_heap:
            print(-hq.heappop(max_heap))
        else:
            print(0)
    else:
        hq.heappush(max_heap, -x)