import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())
for C in range(1, T+1):
    matrix_ = []
    N, K = map(int,(input().split()))
    total_1 = 0
    total_2 = 0
    for i in range(N):
        count_1 = 0
        matrix_.append(input().split())
        for idx in range(N):
            if matrix_[i][idx] == str(1):
                count_1 += 1
            elif matrix_[i][idx] == str(0):
                if count_1 == K:
                    total_1 += 1
                count_1 = 0
        if count_1 == K:
            total_1 += 1
    for i in range(N):
        count_2 = 0 
        for idx in range(N):
            if matrix_[idx][i] == str(1):
                count_2 += 1
            elif matrix_[idx][i] == str(0):
                if count_2 == K:
                    total_2 += 1
                count_2 = 0
        if count_2 == K:
            total_2 += 1
    total = total_1 + total_2
    print(f'#{C}', total)