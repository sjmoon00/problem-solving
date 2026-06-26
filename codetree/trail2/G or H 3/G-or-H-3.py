n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

N = max(x) + 1
arr = [''] * N
for i, char in zip(x, c):
    arr[i] = char

answer = 0
for i in range(1, N - k):
    s = 0
    for ii in range(i, i + k + 1):
        char = arr[ii]
        if char == 'G':
            s += 1
        elif char == 'H':
            s += 2
    answer = max(answer, s)

print(answer)