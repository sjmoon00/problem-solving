n = int(input())
S = input()

dp = {
    'C': [0] * n,
    'CO': [0] * n,
    'COW': [0] * n
}
dp['C'][0] = 1 if S[0] == 'C' else 0

for i in range(1, n):
    dp['C'][i], dp['CO'][i], dp['COW'][i] = dp['C'][i - 1], dp['CO'][i - 1], dp['COW'][i - 1]

    s = S[i]
    if s == 'C':
        dp['C'][i] = dp['C'][i - 1] + 1
    elif s == 'O':
        dp['CO'][i] += dp['C'][i - 1]
    else:
        dp['COW'][i] += dp['CO'][i - 1]

print(dp['COW'][n - 1])