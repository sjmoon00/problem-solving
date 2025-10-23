import sys

input = sys.stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().split()))

low, high = 1, max(trees)

def calc_cut(mid):
    cnt = 0
    for tree in trees:
        if tree > mid:
            cnt += (tree - mid)
    return cnt

while low <= high:
    mid = (low + high) // 2

    cut = calc_cut(mid)
    if cut >= M:
        low = mid + 1
    else:
        high = mid - 1

print(high)