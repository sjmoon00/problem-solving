a = list(input())

# a에 0이 포함된 경우 0중 제일 높은 자리를 1로 바꾸면 됨
if '0' in a:
    for i in range(len(a)):
        if a[i] == '0':
            a[i] = '1'
            break

# a에 0이 없는 경우 1중 제일 낮은 자리를 0으로 바꾸면 됨
else:
    for i in range(len(a) - 1, -1, -1):
        if a[i] == '1':
            a[i] = '0'
            break

print(int(''.join(a), 2))