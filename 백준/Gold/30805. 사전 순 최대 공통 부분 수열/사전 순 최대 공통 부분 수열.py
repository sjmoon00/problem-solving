N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

common_num = set(A) & set(B)
answer = []
while common_num:
    m = max(common_num)
    answer.append(m)

    idx_a = A.index(m)
    idx_b = B.index(m)
    A = A[idx_a+1:]
    B = B[idx_b+1:]
    common_num = set(A) & set(B)

print(len(answer))
if answer:
    print(*answer)