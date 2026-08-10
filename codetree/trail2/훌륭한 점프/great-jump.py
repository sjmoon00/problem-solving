n, k = map(int, input().split())
arr = list(map(int, input().split()))

def is_possible(max_val):
    if arr[0] > max_val or arr[-1] > max_val:
        return False
    
    avail_indices = []
    for i, x in enumerate(arr):
        if x <= max_val:
            avail_indices.append(i)
    
    l = len(avail_indices)
    for i in range(l - 1):
        distance = avail_indices[i+1] - avail_indices[i]
        if distance > k:
            return False
    return True

max_elem = max(arr)
answer = max_elem
for max_val in range(max_elem, 0, -1):
    if is_possible(max_val):
        answer = max_val
    else:
        break

print(answer)