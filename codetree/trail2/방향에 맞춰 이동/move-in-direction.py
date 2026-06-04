n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

pos = [0, 0]
dirs = {'W': (-1, 0), 'S': (0, -1), 'N': (0, 1), 'E': (1, 0)}
for direction, distance in zip(dir, dist):
    pos[0] += dirs[direction][0] * distance
    pos[1] += dirs[direction][1] * distance

print(*pos)