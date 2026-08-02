n = int(input())
arr = list(map(int, input().split()))

answer = 1e9
for i in range(n):
    arr[i] *= 2
    for j in range(n):
        remain_arr = []
        for k in range(n):
            if k != j:
                remain_arr.append(arr[k])
        
        diff_sum = 0
        for k in range(1, len(remain_arr)):
            diff_sum += abs(remain_arr[k] - remain_arr[k - 1])
        
        answer = min(answer, diff_sum)

    arr[i] //= 2

print(answer)