from collections import deque, defaultdict
A, B = map(int, input().split())
INF = 1e9
# dp = [INF] * (B+1)
dp = defaultdict(lambda : INF)
dp[A] = 1
queue = deque([A])
while queue:
    n = queue.popleft()
    if n > B:
        continue
    if n == B:
        break
    
    mul_2 = n * 2
    app_1 = n * 10 + 1
    
    if mul_2 <= B:
        dp[mul_2] = min(dp[mul_2], dp[n] + 1)
        queue.append(mul_2)
    if app_1 <= B:
        dp[app_1] = min(dp[app_1], dp[n] + 1)
        queue.append(app_1)

if dp[B] != INF:
    print(dp[B])
else:
    print(-1)