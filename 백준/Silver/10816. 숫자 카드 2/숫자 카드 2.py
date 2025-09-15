from collections import Counter
import sys
input = sys.stdin.readline
N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

counter = Counter(cards)
for num in nums:
    print(counter[num], end=' ')