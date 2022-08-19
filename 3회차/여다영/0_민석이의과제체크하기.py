import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

for i in range(1, T + 1):
    print(f'#{i}', end = ' ')
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))

    check = dict()
    for k in range(1, N + 1):
        check[k] = 0
    
    for num in nums:
        check[num] = 1
    
    sum = 0
    for j in check:
        if check[j] == 0:
            print(j, end = ' ')
    print()