n = int(input())
S = input()

answer = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if S[i] + S[j] + S[k] == 'COW':
                answer += 1

print(answer)