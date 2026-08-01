X, Y = map(int, input().split())

answer = 0
for n in range(X, Y + 1):
    num = str(n)
    r_num = num[::-1]
    if num == r_num:
        answer += 1

print(answer)