from collections import defaultdict
N = int(input())
employees = list(map(int, input().split()))

tree = defaultdict(list)
for i in range(1, N):
    parent = employees[i]
    tree[parent].append(i)

def get_time(node):
    if not tree[node]:
        return 0
    
    child_times = []
    for child in tree[node]:
        child_times.append(get_time(child))
    
    child_times.sort(reverse=True)

    call_times = []
    for i in range(len(child_times)):
        call_times.append(child_times[i] + (i + 1))

    return max(call_times)

print(get_time(0))