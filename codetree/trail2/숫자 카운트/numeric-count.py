n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

answer = 0
for aa in range(1, 10):
    for bb in range(1, 10):
        if bb == aa: continue
        for cc in range(1, 10):
            if cc == bb or cc == aa: continue

            for num, cnt1, cnt2 in zip(a, b, c):
                num = str(num)
                count1, count2 = 0, 0
                if int(num[0]) == aa: count1 += 1
                if int(num[1]) == bb: count1 += 1
                if int(num[2]) == cc: count1 += 1

                if int(num[0]) != aa and str(aa) in num: count2 += 1
                if int(num[1]) != bb and str(bb) in num: count2 += 1
                if int(num[2]) != cc and str(cc) in num: count2 += 1
                # print((100*aa+10*bb+cc, num), ((count1, count2), (cnt1, cnt2)))
                if not(count1 == cnt1 and count2 == cnt2):
                    break
            else:
                answer += 1

print(answer)
