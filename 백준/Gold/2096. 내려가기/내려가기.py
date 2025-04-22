import sys
input = sys.stdin.readline
N = int(input())
dp_max = [0] * 3
dp_min = [0] * 3
for _ in range(N):
    row = list(map(int, input().split()))
    dp_max = [row[0] + max(dp_max[:2]), row[1] + max(dp_max), row[2] + max(dp_max[1:])]
    dp_min = [row[0] + min(dp_min[:2]), row[1] + min(dp_min), row[2] + min(dp_min[1:])]
print(max(dp_max), min(dp_min))