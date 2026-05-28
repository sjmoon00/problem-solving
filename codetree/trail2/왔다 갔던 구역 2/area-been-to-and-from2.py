n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

arr = [0] * 2001
idx = 1000
dic = {'R': 1, 'L': -1}
for num, d in zip(x, dir):
    for _ in range(num):
        arr[idx] += 1
        idx += dic[d]

print(len([x for x in arr if x > 1]))