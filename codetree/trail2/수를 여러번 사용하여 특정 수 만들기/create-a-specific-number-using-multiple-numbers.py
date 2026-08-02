A, B, C = map(int, input().split())

answer = 0
for x in range(1001):
    a = A * x
    if a > C:
        break
    for y in range(1001):
        num = a + B * y
        if num <= C:
            answer = max(answer, num)
        else:
            break

print(answer)