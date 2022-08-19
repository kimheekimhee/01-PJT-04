# # import sys
# from pprint import pprint
# # sys.stdin = open("_어디에단어가들어갈수있을까.txt")

# t = int(input())

# for test in range(t):
#     n, k = map(int,input().split())
#     cnt1, cnt2 = 0, 0
#     matrix = [(['1'] + list(input().split()) + ['1']) for _ in range(n)]
#     matrix.insert(0,['1']*(n+2))
#     matrix.append(['1']*(n+2))
#     # i = row + 1
#     # j = col + 1   i와j가 확장 전 원래 인덱스
#     for col in range(n):
#         cnt1 += ''.join(*(['1'] + list(input().split()) + ['1'])).count('1'+'0'*k + '1')

#     # 세로 리스트 만들기
#     new_matrix = [list('1'*(n+2)) for _ in range(n+2)]
#     for row in range(n):
#         for col in range(n):
#             new_matrix[row+1][col+1] = matrix[col+1][row+1]
#     for col in range(n):
#         cnt2 += ''.join(*(['1'] + list(input().split()) + ['1'])).count('1'+'0'*k + '1')
#     print(f'#{test+1} {cnt1+cnt2}')

t = int(input())

for test in range(t):
    n, k = map(int,input().split())
    matrix = [list(input().split()) for _ in range(n)]  
    #세로 단어
    cnt_sum_1 = 0
    for row in range(n):
        cnt = 0
        for col in range(n):
            if matrix[col][row] == '1':
                cnt += 1
            else:
                if cnt == k:
                    cnt_sum_1 += 1
                cnt = 0
        if cnt == k:
            cnt_sum_1 += 1

    #가로단어
    cnt_sum_2 = 0
    for col in range(n):
        cnt = 0
        for row in range(n):
            if matrix[col][row] == '1':
                cnt += 1
            else:
                if cnt == k:
                    cnt_sum_2 += 1
                    
                cnt = 0
        if cnt == k:
            cnt_sum_2 += 1
    print(f'#{test+1} {cnt_sum_1+cnt_sum_2}')

        