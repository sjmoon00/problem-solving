from collections import defaultdict
n = int(input())
MOD = 1_000_000_007
dp = defaultdict(int)
dp[0], dp[1], dp[2] = 0, 1, 1

def fibo(n):
    if dp[n] == 0:
        if n & 1 == 0:
            fn = fibo(n // 2)
            fn_m1 = fibo(n // 2 - 1)
            dp[n] = (fn * (fn + 2*fn_m1)) % MOD
        else:
            fn = fibo(n // 2)
            fn_p1 = fibo(n // 2 + 1)
            dp[n] = (fn ** 2 + fn_p1 ** 2) % MOD
    return dp[n]

print(fibo(n))