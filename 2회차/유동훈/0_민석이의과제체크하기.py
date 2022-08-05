import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

for i in range(1, T+1):
    stu, sub = map(int, input().split())
    number = list(map(int, input().split()))
    unsub = list(map(str, range(1, stu+1)))
    
    for j in number:
        unsub.remove(str(j))
    result = ' '.join(unsub)
    print(f'#{i} {result}')