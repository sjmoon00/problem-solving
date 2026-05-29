from collections import defaultdict, Counter
n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

arr = defaultdict(int)
idx = 0
for num, direction in zip(x, dir):
    for i in range(num):
        if direction == 'R':
            arr[idx] = 1 # 검은색

            if i < (num - 1):
                idx += 1
        else:
            arr[idx] = -1 # 흰색

            if i < (num - 1):
                idx -= 1

c = Counter(arr.values())
print(c[-1], c[1])