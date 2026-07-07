from itertools import permutations
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

beautiful = set(permutations(B))
def main():
    if N < M:
        print(0)
        return
    
    answer = 0
    for i in range(N - M + 1):
        part = tuple(A[i:i + M])
        if part in beautiful:
            answer += 1
    
    print(answer)

main()