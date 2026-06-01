n, t = map(int, input().split())
arr = list(map(int, input().split()))

cnt, answer = 0, 0
for i in range(n):
    if arr[i] > t:
        cnt += 1
        answer = max(answer, cnt)
    else:
        cnt = 0

print(answer)