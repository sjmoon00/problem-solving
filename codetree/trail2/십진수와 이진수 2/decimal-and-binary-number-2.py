N = input()

num = int(N, 2)
num = (num << 4) + num

print(format(num, 'b'))