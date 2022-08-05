# N x N 배열. 숫자는 파리갯수.
# M x M 파리채를 내리쳐서 많이 잡기.
# N 5~15 M 2~N 파리 칸당30이하.

# import sys

# # sys.stdin = open("_파리퇴치.txt")

# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#     list_N = []
#     for i in range(N):
#         list_N.append(list(map(int, input().split())))      # NxN 행렬 만들기.
#     # MxM 범위를 탐색하려면 델타이동을 써야할까??? (아닌듯?)
#     #잘 모르겠지만.. 일단 MxM 범위를 탐색 했을때 NxN을 안벗어나는게 중요해보임. (조건1)
#     #그리고, i,j에서부터~ i+M, j+M 의 영역까지 합을 구해야함... (조건2) -> ************************** 어떻게할지 모르겠음.. 변수가 더필요한거같음..

#     sum_list = [] #i,j에서 MxM 파리채를 휘둘렀을때 잡히는 파리수를 모아놓은 리스트
#     sum_ = 0

#     for i in range(N):
#         for j in range(N):
#             for x in range(i, i + M + 1):
#                 for y in range(j, j + M + 1):
#                     if x + M <= N and y + M <= N :   # 조건1
#                         sum_ += list_N[x][y]
#             sum_list.append(sum_)    
#             sum_ = 0

#     print(sum_list) 

#     # for i in range(N):
#     #     for j in range(M):
#     #         if i + M <= N - 1 and j + M <= N - 1:
#     #             sum_[i][j] = list_N[i][j]
    
#     포기


# N x N 배열. 숫자는 파리갯수.
# M x M 파리채를 내리쳐서 많이 잡기.
# N 5~15 M 2~N 파리 칸당30이하.

T = int(input())
for i in range(1, T+1):
    N, M = map(int, input().split())

    list_ = []
    for i in range(N):
        list_.append(list(map(int, input().split())))

    d_x = list(range(M-1))
    d_y = list(range(M-1))
    sum_list = []
    sum_ = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            sum_ += list_[i][j]
           
        # 델타이동? 써야하는것 같은데 어떻게하는지 아직 모르겠음
    
            