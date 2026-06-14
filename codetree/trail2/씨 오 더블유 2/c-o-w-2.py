n = int(input())
S = input()

c, co, cow = 0, 0, 0
for s in S:
    if s == 'C':
        c += 1
    elif s == 'O':
        co += c
    else:
        cow += co

print(cow)