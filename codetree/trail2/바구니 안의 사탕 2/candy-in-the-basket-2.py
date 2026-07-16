N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

arr = [0] * 101
for p, c in zip(pos, candy):
    arr[p] += c

answer = 0
for mid in range(101):
    start, end = mid-K, mid + (K+1)
    if start < 0:
        start = 0
    if end > 100:
        end = 100
    
    cnt = 0
    for i in range(start, end):
        cnt += arr[i]
    
    answer = max(answer, cnt)

print(answer)
