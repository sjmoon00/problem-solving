A, B, C = map(int, input().split())

answer = 0
# 1. 1001 대신 C // A + 1로 정확한 범위를 지정
for x in range(C // A + 1):
    a = A * x
    
    # 2. y를 0부터 1씩 올리는 루프 대신, 남은 공간에 들어갈 수 있는 B의 최대 개수를 계산
    y = (C - a) // B
    num = a + B * y
    
    answer = max(answer, num)

print(answer)