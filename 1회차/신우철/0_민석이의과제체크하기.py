import sys
#b.sort(reverse=False)
sys.stdin = open("_민석이의과제체크하기.txt")
T = int(input())
for test in range(1, T+1):
    x,y = map(int,input().split())
    # x 명중 y명이 제출하지 않음
    a = []
    z = list(map(int,input().split()))
    # 과제를 제출한사람 입력
    for i in range(1, x+1):
            
        # x= 1 ~ x+1
        if i not in z:
            a.append(i)

    print(f'#{test}', *a)
        