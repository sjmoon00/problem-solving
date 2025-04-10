T = int(input())
for _ in range(T):
    N = int(input())
    dp = [(0, 0)] * (N + 1)
    
    def fibo(n):
        if dp[n] != (0, 0):
            return dp[n]
        
        if n == 0:
            dp[0] = (1, 0)
            return dp[0]
        elif n == 1:
            dp[1] = (0, 1)
            return dp[1]
        else:
            a = fibo(n-1)
            b = fibo(n-2)
            dp[n] = (a[0]+b[0], a[1]+b[1])
            return dp[n]
    
    answer = fibo(N)
    print(answer[0], answer[1])