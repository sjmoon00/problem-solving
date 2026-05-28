n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

arr = [0] * 2001
idx = 1000
for num, d in zip(x, dir):
    for _ in range(num):
        if d == 'R':
            arr[idx] += 1
            idx += 1
        else:
            idx -= 1
            arr[idx] += 1

print(sum(1 for x in arr if x > 1))