n, t = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 1 if arr[0] > t else 0
answer = cnt
for i in range(1, n):
    if arr[i] > t:
        cnt += 1
        answer = max(answer, cnt)
    else:
        cnt = 0

print(answer)