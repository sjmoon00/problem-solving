T, a, b = map(int, input().split())
arr = []
for _ in range(T):
    char, pos = input().split()
    arr.append((int(pos), char))

answer = 0
for k in range(a, b + 1):
    d1, d2 = 1e9, 1e9
    for i, c in arr:
        if c == 'S':
            d1 = min(d1, abs(k - i))
        else:
            d2 = min(d2, abs(k - i))

    if d1 <= d2:
        answer += 1

print(answer)