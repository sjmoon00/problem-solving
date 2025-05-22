import math
X = 1_000_000_007
M = int(input())
answer = 0
for i in range(M):
    n, s = map(int, input().split())
    gcd = math.gcd(s, n)
    n, s = n//gcd, s//gcd
    answer = (answer + (s * pow(n, -1, X)) % X) % X
print(answer)