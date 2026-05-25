m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

end = sum(days[1:m2]) + d2
start = sum(days[1:m1]) + d1
print(end - start + 1)