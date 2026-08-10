N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

min_elem, max_elem = min(arr), max(arr)
answer = 0
for begin in range(min_elem, max_elem + 1):
    end = begin + K
    cnt = 0
    for x in arr:
        if begin <= x <= end:
            cnt += 1
    answer = max(answer, cnt)

print(answer)