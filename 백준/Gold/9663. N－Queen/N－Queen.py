N = int(input())
dp = [0] * N
cnt = 0

def is_safe(x):
    for i in range(x):
        if dp[x] == dp[i]:
            return False
        if abs(dp[x] - dp[i]) == abs(x - i):
            return False
    return True

def dfs(depth):
    global cnt
    if depth == N:
        cnt += 1
        return
    
    for i in range(N):
        dp[depth] = i
        if is_safe(depth):
            dfs(depth + 1)
        
dfs(0)
print(cnt)