N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

cnt = 0
for coin in coins[::-1]:
    if coin > K:
        continue

    cnt += K // coin
    K %= coin
print(cnt)