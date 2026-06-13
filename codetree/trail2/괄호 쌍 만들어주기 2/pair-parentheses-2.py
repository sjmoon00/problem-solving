A = input()

N = len(A)
answer = 0
for i in range(N - 3):
    if A[i] + A[i + 1] != '((': continue
    for j in range(i + 2, N - 1):
        if A[j] + A[j + 1] == '))':
            answer += 1

print(answer)