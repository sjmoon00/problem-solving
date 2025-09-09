from collections import defaultdict
T = int(input())
for _ in range(T):
    N = int(input())
    d = defaultdict(set)
    for _ in range(N):
        name, category = input().split()
        d[category].add(name)
    
    answer = 1
    for clothes in d:
        answer *= len(d[clothes])+1
    print(answer-1)