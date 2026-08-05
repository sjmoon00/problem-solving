n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

answer = 0
for start_idx in range(1, n + 1):
    i = start_idx
    acc = 0
    for _ in range(m):
        value = arr[i]
        acc += value
        i = value
    answer = max(answer, acc)

print(answer)