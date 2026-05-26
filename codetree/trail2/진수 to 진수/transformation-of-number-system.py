a, b = map(int, input().split())
n = input()

n = int(n, a)

nums = []
while True:
    if n < b:
        nums.append(n)
        break

    nums.append(n % b)
    n //= b

print(''.join(map(str, nums[::-1])))