n = int(input())
adjacent = list(map(int, input().split())) if n >= 2 else []

def main():
    if n == 1:
        print(*adjacent)
        return
    
    for a1 in range(1, n+1):
        arr = [a1]
        visited = [False] * (n + 1)
        visited[a1] = True
        for i in range(n-1):
            s = adjacent[i]
            a_i1 = s - arr[i]
            if visited[a_i1]:
                break
            visited[a_i1] = True
            arr.append(a_i1)
        else:
            print(*arr)
            return

main()