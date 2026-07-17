N = int(input())
a, b, c = map(int, input().split())

answer = 0
for aa in range(1, N + 1):
    for bb in range(1, N + 1):
        for cc in range(1, N + 1):
            if abs(a - aa) <= 2 or abs(b - bb) <= 2 or abs(c - cc) <= 2:
                answer += 1

print(answer)