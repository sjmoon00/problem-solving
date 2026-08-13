nums = list(map(int, input().split()))
nums.sort()

def is_equal(arr1, arr2):
    for n1, n2 in zip(arr1, arr2):
        if n1 != n2:
            return False
    return True

found = False
for a in range(1, 41):
    for b in range(a, 41):
        for c in range(b, 41):
            for d in range(c, 41):
                arr = [a, b, c, d, a+b, b+c, c+d, d+a, a+c, b+d, a+b+c, a+b+d, a+c+d, b+c+d, a+b+c+d]
                arr.sort()
                
                if is_equal(nums, arr):
                    print(a, b, c, d)
                    found = True
                    break
            if found: break
        if found: break
    if found: break
