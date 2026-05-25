m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
D1 = sum(days[:m1]) + d1
D2 = sum(days[:m2]) + d2

gap = D2 - D1

week = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 
        'Fri': 4, 'Sat': 5, 'Sun': 6}
print(((gap - week[A]) // 7) + 1)