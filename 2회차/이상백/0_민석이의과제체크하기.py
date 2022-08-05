# import sys

# sys.stdin = open("_민석이의과제체크하기.txt", 'r')

T = int(input())

for test in range(1, T+1):

    N, K = map(int, input().split())

    submit = list(map(int,input().split()))

    matrix = []

    for i in range(1, N+1):
        # 1 2 3 4 5
        if i not in submit:
            matrix.append(i)
# print(f' #{test} {*matrix}')
    print('#{}'.format(test), *matrix)
