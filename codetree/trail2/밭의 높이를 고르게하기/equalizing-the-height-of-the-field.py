N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

answer = 1e9
for start in range(N - T):
    cnt = 0
    for i in range(start, start + T):
        h = arr[i]
        cnt += abs(h - H)
    answer = min(answer, cnt)

print(answer)