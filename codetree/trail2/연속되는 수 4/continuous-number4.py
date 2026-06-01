n = int(input())
arr = [int(input()) for _ in range(n)]

cnt, answer = 1, 1
for i in range(n):
    if i > 0 and (arr[i] > arr[i - 1]):
        cnt += 1
        answer = max(answer, cnt)
    else:
        cnt = 1

print(answer)