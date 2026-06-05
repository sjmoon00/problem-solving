commands = input()

x, y = 0, 0
dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
curr_dir = 0
time = 0
for command in commands:
    if command == 'R':
        curr_dir = (curr_dir + 1) % 4
    elif command == 'L':
        curr_dir = (curr_dir + 4 - 1) % 4
    else:
        dx, dy = dxy[curr_dir][0], dxy[curr_dir][1]
        x += dx
        y += dy
    time += 1
    if (x, y) == (0, 0):
        print(time)
        break
else:
    print(-1)