N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

answer = 0
for a in range(1, N + 1):
    for b in range(1, N + 1):
        for c in range(1, N + 1):
            if min(abs(a - a1), N - abs(a - a1)) <= 2 and \
            min(abs(b - b1), N - abs(b - b1)) <= 2 and \
            min(abs(c - c1), N - abs(c - c1)) <= 2:
                answer += 1
            elif min(abs(a - a2), N - abs(a - a2)) <= 2 and \
            min(abs(b - b2), N - abs(b - b2)) <= 2 and \
            min(abs(c - c2), N - abs(c - c2)) <= 2:
                answer += 1

print(answer)
