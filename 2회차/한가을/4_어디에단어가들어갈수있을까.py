# N x N 크기의 단어 퍼즐을 만들려고 한다
# 입력으로 단어 퍼즐의 모양이 주어짐
# 주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가
# 들어갈 수 있는 자리의 수를 출력

# 첫 줄에 총 테스트 케이스의 개수 T가 온다
# 다음 줄부터 각 테스트 케이스가 주어진다
# 테스트 케이스의 첫번째 줄에는
# 단어 퍼즐의 가로, 세로 길이 N과 단어의 길이 K가 주어진다
# 두 번째 줄부터 퍼즐의 모양이 2차원 정보로 주어진다
# 퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0

# 출력 예시
#1 2
#2 6
#3 6
#4 0
#5 14
#6 2
#7 45
#8 0
#9 98
#10 7

import sys
sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())

for tc in range(1,T+1):
    N,K = map(int,input().split())
    arr = []

    for i in range(N):
        arr.append(list(map(int, input().split())))

    #배열 받기
    result = 0
    cnt = 0

    #가로 탐색
    for x in range(N):
        # 행(x) 기준
        for y in range(N):
            if arr[x][y] == 1:
                cnt += 1
            # 0을 만났거나 벽을 만났을 때
            if arr[x][y] == 0 or y == N-1:
                # 이전에 계산한 카운트가 k라면 result에 카운트
                if cnt == K:
                    result += 1
                # 카운트 초기화
                cnt = 0

    # 세로 탐색
    for y in range(N):
        # 열(y)기준
        for x in range(N):
            #1이면 카운트
            if arr[x][y] == 1:
                cnt += 1
            if arr[x][y] == 0 or x == N-1 :  
                if cnt == K:
                    result += 1
                cnt = 0

    print('#{} {}'.format(tc,result ))