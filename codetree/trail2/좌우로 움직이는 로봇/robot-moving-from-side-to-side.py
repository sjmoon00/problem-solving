n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)
 
#  Please write your code here.
A = [0]
for time, direction in zip(t, d):
    if direction == 'R':
        for _ in range(time):
            A.append(A[-1] + 1)
    else:
        for _ in range(time):
            A.append(A[-1] - 1)

B = [0]
for time, direction in zip(t_b, d_b):
    if direction == 'R':
        for _ in range(time):
            B.append(B[-1] + 1)
    else:
        for _ in range(time):
            B.append(B[-1] - 1)

diff = abs(len(A) - len(B))
if len(A) < len(B):
    A.extend([A[-1]] * diff)
else:
    B.extend([B[-1]] * diff)

prev_a, prev_b, answer = 0, 0, 0
for i in range(1, len(A)):
    a, b = A[i], B[i]
    if a == b and prev_a != prev_b:
        answer += 1
    
    prev_a, prev_b = a, b

print(answer)