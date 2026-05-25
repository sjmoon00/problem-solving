a, b, c = map(int, input().split())

# Please write your code here.
def main():
    if a < 11:
        print(-1)
        return
    if b < 11:
        print(-1)
        return
    if c < 11:
        print(-1)
        return
    
    print((a*60*24 + b*60 + c) - (11*60*24 + 11*60 + 11))

main()