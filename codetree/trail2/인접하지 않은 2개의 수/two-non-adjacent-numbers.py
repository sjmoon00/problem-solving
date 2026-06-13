n = int(input())
numbers = list(map(int, input().split()))

answer = 0
left_max = numbers[0]
for i in range(2, n):
    num = numbers[i]
    answer = max(answer, left_max + num)

    left_max = max(left_max, numbers[i - 1])

print(answer)