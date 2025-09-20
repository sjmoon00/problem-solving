from collections import Counter
import math
def solution(weights):
    answer = 0
    ratio = [(2, 3), (2, 4), (3, 4)]
    counter = Counter(weights)
    for k, v in counter.items():
        if v > 1:
            answer += math.comb(v, 2)
    
    W = set(weights)
    for w in W:
        for a, b in ratio:
            r = w * (a/b)
            if r in W:
                answer += counter[w] * counter[r]

    return answer