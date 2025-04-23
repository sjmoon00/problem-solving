from collections import Counter
def trans_bi(n):
    arr = []
    while n != 1:
        r = n % 2
        n //= 2
        arr.append(str(r))
    arr.append(str(n))
    return ''.join(arr[::-1])

def solution(s):
    trans_cnt = 0
    zero_cnt = 0
    while s != '1':
        cntr = Counter(s)
        if '0' not in cntr:
            cntr['0'] = 0
        if '1' not in cntr:
            cntr['1'] = 0
        zero_cnt += cntr['0']
        trans_cnt += 1
        s = trans_bi(cntr['1'])

    return [trans_cnt, zero_cnt]