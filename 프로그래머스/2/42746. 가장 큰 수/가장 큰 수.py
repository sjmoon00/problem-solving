def solution(numbers):
    answer = []
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    for x in numbers:
        answer.append(x)
    return str(int(''.join(answer)))