import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())
for t in range(1, T+1):
    n, k = map(int,input().split())
    puzzle = [list(map(int,input().split())) for _ in range(n)]
    
    result = 0

    # 행 검사
    for i in range(n):
        # 빈공간 세기
        cnt = 0
        for j in range(n):
            # 만약 1이면 빈공간 1추가
            if puzzle[i][j] == 1:
                cnt += 1

            # 만약 0이거나 마지막 부분 일 때,
            if puzzle[i][j] == 0 or j == n-1:
                # 빈공간 수가 k와 같다면
                if cnt == k:
                    # 결과값 1 추가
                    result += 1
                # 빈공간 초기화
                cnt = 0

        # 열 검사, 행과 같은 방식
        for j in range(n):
            if puzzle[j][i] == 1:
                cnt += 1

            if puzzle[j][i] == 0 or j == n-1:
                if cnt == k:
                    result += 1
                cnt = 0

    print(f'#{t}', result)