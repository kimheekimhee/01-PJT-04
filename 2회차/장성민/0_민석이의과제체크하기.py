import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())


for tc in range(1, T + 1):
    n, k = map(int, input().split())

    students = list(map(int, input().split()))
    
    x_total = []
 
    for i in range(1, n + 1):
        if i not in students:
            x_total.append(i)

    print(f'#{tc}', *x_total)