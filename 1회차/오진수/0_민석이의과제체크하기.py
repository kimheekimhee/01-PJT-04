import sys

sys.stdin = open("_민석이의과제체크하기.txt")


t = int(input())

for tc in range(1, t + 1) :
    total_, submit_ = map(int, input().split())
    num_ = list(map(int, input().split()))
    list_ = []

    for i in range(1, total_+ 1) : #range(total)
        if i not in num_ :
            list_.append(i)
    
    print(f'#{tc}', *list_) #들여쓰기?