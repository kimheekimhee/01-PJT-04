# import sys

# sys.stdin = open("_파리퇴치.txt")

# T = int(input())
T = 1
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    list_ = [list(map(int, input().split())) for _ in range(N)]
    # print(list_)

    sum_ = 0
    sum_list =[]
    
    
    # 0부터 N-M까지
    for i in range(N-M+1):
        # 0부터 N-M까지
        for j in range(N-M+1):
            #for k in range(M):
            sum_ = list_[i][j] + list_[i][j+1] + list_[i+1][j] + list_[i+1][j+1]
            sum_list.append(sum_)
    print(sum_list)

    print(f'#{test_case} {max(sum_list)}')