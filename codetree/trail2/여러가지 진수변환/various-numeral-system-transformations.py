N, B = map(int, input().split())

nums = []
while True:
    if N < B:
        nums.append(N)
        break
    
    nums.append(N % B)
    N //= B

print(''.join(map(str, nums[::-1])))