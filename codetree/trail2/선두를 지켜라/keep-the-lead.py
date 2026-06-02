n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
A = [0]
for v_a, t_a in zip(v, t):
    for _ in range(t_a):
        A.append(A[-1] + v_a)

B = [0]
for v_b, t_b in zip(v2, t2):
    for _ in range(t_b):
        B.append(B[-1] + v_b)

lead, cnt = '', 0
for i in range(1, len(A)):
    a, b = A[i], B[i]

    if a > b and lead != 'A':
        if lead == '':
            lead = 'A'
            continue
        lead = 'A'
        cnt += 1
    elif b > a and lead != 'B':
        if lead == '':
            lead = 'B'
            continue
        lead = 'B'
        cnt += 1

print(cnt)