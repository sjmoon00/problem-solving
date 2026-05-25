n = int(input())

nums = []
while True:
    if n < 2:
        nums.append(n)
        break
    
    nums.append(n % 2)
    n //= 2

print(''.join(map(str, reversed(nums))))