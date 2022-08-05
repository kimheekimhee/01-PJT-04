from pprint import pprint

import sys
sys.stdin = open("_파리퇴치.txt")

# 델타 순회

T = int(input())

for t in range(1, T+1):
    # N: 배열 크기, M: 파리채 크기
    N, M = map(int, input().split()) 

    # 매트릭스 생성
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))


    result = []
    for i in range(N): ########## 마지막 줄 반복할 필요X
        for j in range(N):

        # 파리채: 델타 범위 설정
            score = 0
            for ii in range(i, i+M):
                for jj in range(j, j+M):
                    # 델타 범위 제한
                    if 0 <= ii <= N-1 and 0 <= jj <= N-1:
                        score += matrix[ii][jj]
            result.append(score)
    print(f"#{t} {max(result)}")