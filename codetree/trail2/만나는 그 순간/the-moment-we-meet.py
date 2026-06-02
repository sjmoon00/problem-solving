n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

A = [0]
for direction, time in zip(d, t):
    if direction == 'L':
        for _ in range(time):
            A.append(A[-1] - 1)
    else:
        for _ in range(time):
            A.append(A[-1] + 1)

B = [0]
for direction, time in zip(d2, t2):
    if direction == 'L':
        for _ in range(time):
            B.append(B[-1] - 1)
    else:
        for _ in range(time):
            B.append(B[-1] + 1)

answer = -1
for i, (a, b) in enumerate(zip(A, B)):
    if i != 0 and a == b:
        answer = i
        break
print(answer)