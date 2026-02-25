code = input()
N = len(code)

def is_between_10_26(i):
    if 10 <= int(code[i-2: i]) <= 26:
        return True
    else:
        return False

if code[0] == '0':
    print(0)
else:
    dp = [0] * (N + 1)

    dp[0] = 1
    dp[1] = 1
    

    for i in range(2, N+1):
        if code[i-1] != '0':
            dp[i] += dp[i-1]
        
        if is_between_10_26(i):
            dp[i] += dp[i-2]

    print(dp[-1] % 1_000_000)