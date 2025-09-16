import sys
nums = list(map(int, sys.stdin.readlines()))
def kt_set(string):
    n = len(string)
    if n == 1:
        return '-'
    if n == 3:
        return '- -'
    
    dn = n // 3
    s = kt_set('-' * dn)
    return s + (' ' * dn) + s

for N in nums:
    print(kt_set('-' * (3**N)))