N = int(input())
arr = [int(input()) for _ in range(N)]

cnt, answer = 0, 0
for i in range(N):
    if i > 0 and (arr[i] * arr[i - 1] > 0):
        cnt += 1
    else:
        cnt = 1
    
    answer = max(answer, cnt)

print(answer)