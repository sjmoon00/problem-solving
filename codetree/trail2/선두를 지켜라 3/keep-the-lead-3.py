N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
A = [0]
for va, ta in zip(v, t):
    for _ in range(ta):
        A.append(A[-1] + va)

B = [0]
for vb, tb in zip(v2, t2):
    for _ in range(tb):
        B.append(B[-1] + vb)

diff = abs(len(A) - len(B))
if len(A) < len(B):
    A.extend([A[-1]] * diff)
else:
    B.extend([B[-1]] * diff)

lead, answer = '', 0
for i in range(1, len(A)):
    a, b = A[i], B[i]
    if a > b and lead != 'A':
        lead = 'A'
        answer += 1
    elif b > a and lead != 'B':
        lead = 'B'
        answer += 1
    elif a == b and lead != 'AB':
        lead = 'AB'
        answer += 1
        
print(answer)