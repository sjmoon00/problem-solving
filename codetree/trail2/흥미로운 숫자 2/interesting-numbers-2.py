from collections import Counter
X, Y = map(int, input().split())

answer = 0
for n in range(X, Y + 1):
    nums = list(map(int, str(n)))
    c = Counter(nums)
    if len(c) == 2 and 1 in c.values():
        answer += 1

print(answer)