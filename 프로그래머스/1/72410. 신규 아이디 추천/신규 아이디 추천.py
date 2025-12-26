def solution(new_id):
    string1 = stage1(new_id)
    string2 = stage2(string1)
    string3 = stage3(string2)
    string4 = stage4(string3)
    string5 = stage5(string4)
    string6 = stage6(string5)
    answer = stage7(string6)
    return answer

def stage1(s: str) -> str:
    return s.lower()

def stage2(s: str) -> str:
    tmp = []
    for x in s:
        if not x.isalnum() and x not in ['-', '_', '.']:
            continue
        tmp.append(x)
    return ''.join(tmp)

def stage3(s: str) -> str:
    tmp, last = [], ''
    for x in s:
        if x == last == '.':
            continue
        tmp.append(x)
        last = x
    return ''.join(tmp)

def stage4(s: str) -> str:
    tmp, N = [], len(s)
    for i in range(N):
        x = s[i]
        if (i == 0 or i == N-1) and x == '.':
            continue
        tmp.append(x)
    return ''.join(tmp)

def stage5(s: str) -> str:
    return 'a' if not s else s

def stage6(s: str) -> str:
    N = len(s)
    if N >= 16:
        tmp = list(s[:15])
        if tmp[-1] == '.':
            tmp.pop()
        return ''.join(tmp)
    else:
        return s

def stage7(s: str) -> str:
    N = len(s)
    if N <= 2:
        l = s[-1]
        s += (3 - N) * l
        return s
    else:
        return s
