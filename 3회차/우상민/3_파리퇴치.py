#import sys

#sys.stdin = open("_파리퇴치.txt")

T = int(input())
for T in range(1, T+1):
    N, M = map(int,(input().split()))
    total = 0
    matrix_ = []
    for i in range(1, N+1):  #1 ~ 5
        matrix_.append(list(map(int, (input().split()))))
    for idx in (range((N-(M-1)))):  # 0 ~ 3
        for index in (range((N-(M-1)))):   # 0 ~ 3
            Ch = 0
            Oh = 0
            count = 0   
            for i_ in range((M**2)+M): # 0 ~ 8
                if Ch == M:
                    Ch = 0
                    Oh += 1
                elif Ch < M:
                    count += matrix_[idx+Oh][index+Ch]
                    Ch += 1
            if count > total:
                total = count
    print(f'#{T}', total)

