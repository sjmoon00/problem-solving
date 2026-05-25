a, b, c = map(int, input().split())

# Please write your code here.
def main():
    target = a*60*24 + b*60 + c
    base = 11*60*24 + 11*60 + 11
    if target < base:
        print(-1)
        return

    print(target - base)

main()