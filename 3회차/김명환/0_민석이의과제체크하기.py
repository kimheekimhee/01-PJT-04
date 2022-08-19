import sys
sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())
for i in range(T):
    N, K = map(int,input().split()) # 순서대로 총인원, 과제 낸 사람
    num_list = list(map(int,input().split()))
    result = []
    for j in range(N):
        if j + 1 not in num_list:
            result.append(j + 1)
    print(f'#{i+1}', end=' ')
    print(*result)