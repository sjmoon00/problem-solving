T = int(input())
for _ in range(T):
    N = int(input())
    stickers = []
    for _ in range(2):
        row = list(map(int, input().split()))
        stickers.append(row)
    
    dp = [[0] * N for _ in range(2)]
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]

    if N > 1:
        dp[0][1] = stickers[0][1] + stickers[1][0]
        dp[1][1] = stickers[1][1] + stickers[0][0]
    for i in range(2, N):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + stickers[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + stickers[1][i]

    print(max(dp[0][-1], dp[1][-1]))