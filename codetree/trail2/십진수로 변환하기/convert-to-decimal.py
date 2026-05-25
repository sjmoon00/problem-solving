binary = input()

answer = 0
for b in binary:
    answer = (answer << 1) + int(b)
print(answer)