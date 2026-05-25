m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
D1 = sum(days[:m1]) + d1
D2 = sum(days[:m2]) + d2

gap = D2 - D1

d = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
print(d[gap % 7])