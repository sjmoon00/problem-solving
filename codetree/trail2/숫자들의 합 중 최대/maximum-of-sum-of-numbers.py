X, Y = map(int, input().split())

answer = 0
for n in range(X, Y + 1):
    numbers = list(map(int, list(str(n))))
    answer = max(answer, sum(numbers))

print(answer)