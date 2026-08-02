n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]

answer = 0
for init_stone in range(1, 4):
    stone = init_stone
    cnt = 0
    for a, b, c in moves:
        if stone in [a, b]:
            stone = (a + b) - stone
        if stone == c:
            cnt += 1
    answer = max(answer, cnt)

print(answer)