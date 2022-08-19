import sys
sys.stdin = open("_어디에단어가들어갈수있을까.txt")

# NxN 퍼즐. 검은색엔 못들어감. 길이 K단어가 들어갈수있는 자리 수 출력하기.
# 흰곳 1 검은곳  0임. 길이가 딱맞아야들어감.

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = []
    for i in range(N):
        puzzle.append(list(map(int, input().split())))
    
    #범위조건을 만족할때, 연속된 흰블럭갯수가 k면 count를 1 늘린다

    count_row = 0
    serial = 0 #연속된 흰블럭개수

    #가로
    for i in range(N):
        for j in range(N):
            # if j + K <= N: #범위설정. 저 범위를 넘어서면 퍼즐밖을나감 << 이 문제는 범위조건이 필요없는 문제였음..
            if puzzle[i][j] == 1:
                serial += 1
            else:
                if serial == K:
                    count_row += 1
                serial = 0
        if serial == K:
            count_row += 1
        serial = 0

    serial = 0
    count_col = 0   
    for i in range(N):
        for j in range(N):            
            if puzzle[j][i] == 1:
                serial += 1
            else:
                if serial == K:
                    count_col += 1
                serial = 0
        if serial == K:
            count_col += 1
        serial = 0
    
    count = count_col + count_row

    print(f'#{test_case} {count}')
