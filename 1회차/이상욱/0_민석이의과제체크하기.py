import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

for i in range(1, T+1):
# 첫번째줄 수강생수 / 과제 제출한 사람의 수(N / K)
# 두번째줄 과제 제출한 사람의 번호 K개 
    N, K = map(int, input().split())
    sub = list(map(int, input().split()))
    rest = []

    for j in range(1, N+1):
        if j not in sub:
            rest.append(j)

    print(f'#{i}' , end = ' ')
    for k in range(len(rest)):
        print(f'{rest[k]}' , end= ' ')
    print()
    