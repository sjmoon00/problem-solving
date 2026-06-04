dirs = input()

x, y = 0, 0
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
i = 0
for command in dirs:
    if command == 'L':
        i = (i - 1) % 4
    elif command == 'R':
        i = (i + 1) % 4
    else:
        x += d[i][0]
        y += d[i][1]

print(x, y)
