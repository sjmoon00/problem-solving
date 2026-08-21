N = int(input())
heights = [int(input()) for _ in range(N)]

answer = float('inf')
for lower_bound in range(101):
    upper_bound = lower_bound + 17
    cost = 0
    for height in heights:
        if height > upper_bound:
            cost += (height - upper_bound) ** 2
        elif height < lower_bound:
            cost += (lower_bound - height) ** 2
    
    answer = min(answer, cost)
        
print(answer)