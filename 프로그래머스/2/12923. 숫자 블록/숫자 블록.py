from math import sqrt
def solution(begin, end):
    answer = {x:1 for x in range(begin, end+1)}
    if begin == 1:
        answer[begin] = 0
    N = end - begin + 1
    
    def getMaxDiv(n):
        if n == 1:
            return 0
        elif n <= 3:
            return 1

        tmp = []
        for i in range(2, int(sqrt(n)) + 1):
            if n%i == 0:
                d = int(n/i)
                if d <= 10000000:
                    return d
                else:
                    tmp.append(i)
        if tmp:
            return tmp[-1]
        return 1


    for i in range(begin, end+1):
        max_div = getMaxDiv(i)
        if max_div != None:
            answer[i] = max_div

    # for i in range(begin, N//2 + 1):
    #     mul = 2
    #     idx = i * mul
    #     while idx <= end:
    #         answer[idx] = i
    #         mul += 1
    #         idx = i * mul

    return list(answer.values())