N, B = map(int, input().split())
arr = []
for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)

b = format(B, 'b')
answer = [[1 if i == j else 0 for j in range(N)] for i in range(N)]

def mat_mult(A, B):
    tmp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                tmp[i][j] = (tmp[i][j] + A[i][k] * B[k][j]) % 1000
    return tmp

for x in b[::-1]:
    if x == '1':
        answer = mat_mult(answer, arr)
    arr = mat_mult(arr, arr)

for x in answer:
    print(*x)