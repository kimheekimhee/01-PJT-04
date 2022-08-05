from pprint import pprint

import sys
sys.stdin = open("_어디에단어가들어갈수있을까.txt")

# 0 카운트하면서 길이 저장
# 길이가 일치하면, 매트릭스 갱신하고, result +=1

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split()) # N: 퍼즐 크기, K: 단어의 길이

    # 매트릭스 생성
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    # 매트릭스 순회하며 단어가 몸 뉘일 자리 찾기

    result = [0, 0]

    for i in range(N):
        x_cnt, y_cnt = 0, 0

        x_cnt_list = []
        y_cnt_list = []
        for j in range(N):
            # 가로
            if matrix[i][j] == 1:
                x_cnt += 1
                x_cnt_list.append(x_cnt)
            else:
                x_cnt = 0


            # 세로
            if matrix[j][i] == 1:
                y_cnt += 1
                y_cnt_list.append(y_cnt)
            else:
                y_cnt = 0
                
        if max(x_cnt_list) == 3:
            result[0] += 1
        if max(y_cnt_list == 3):
            result[1] += 1
            
        print(x_cnt_list)
        print(y_cnt_list)
        print("===========")
    print("***********")