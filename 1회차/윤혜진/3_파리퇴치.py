# D2-파리퇴치



# 입력
'''
1. 테스트 케이스 수 T
2. 그리드 크기 N, 파리채 크기 M
- 5 <= N <= 15
- 2 <= M <= N
3. N줄에 걸쳐 N x N 배열
'''



# 출력
'''
1. #{해당 테스트케이스} + {M x M 크기의 파리채를 한 번 내리쳐 죽일 수 있는 파리 최댓값}
'''



# 코드 1
import sys

sys.stdin = open("input_text/_파리퇴치.txt")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]   # N x N 그리드

    # M x M 크기의 파리채로 내리쳐 파리를 죽임
    max_killed = 0   # 죽인 파리 갯수 최댓값
    for r in range(N - M + 1):
        for c in range(N - M + 1):
            killed_fly = 0   # 현 위치에서 죽일 수 있는 파리 갯수

            # M x M 크기 내 파리 죽이기
            for ver in range(M):
                killed_fly += sum(grid[r + ver][c:c + M]) 
            
            # max_killed 값과 크기 비교
            if killed_fly > max_killed:
                max_killed = killed_fly

    print(f'#{test_case} {max_killed}')



# 실행결과(메모리:60,632 kb, 시간:153 ms)



# 코드 2
import sys
from itertools import accumulate

sys.stdin = open("input_text/_파리퇴치.txt")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]   # N x N 그리드
    
    # 행 누적합
    grid = [[0] + list(accumulate(row)) for row in grid]
    
    # 행 누적합 한 것을 다시 열 누적합
    grid = [[0] + list(accumulate(row)) for row in zip(*grid)]

    new_grid = [[0] * (N + 1) for _ in range(N + 1)]   # grid를 행렬 반전시킨 것
    for r in range(N + 1):
        for c in range(N + 1):
            new_grid[c][r] = grid[r][c] 
    
    # M x M 크기의 파리채로 내리쳐 죽일 수 있는 최대 파리 갯수
    max_killed = 0
    for r in range(M, N + 1):
        for c in range(M, N + 1):
            # 현 위치에서 죽일 수 있는 파리 갯수
            killed_fly = new_grid[r][c] - new_grid[r][c - M] - new_grid[r - M][c] + new_grid[r - M][c- M]

            # max_killed 값과 크기 비교
            if killed_fly > max_killed:
                max_killed = killed_fly

    print(f'#{test_case} {max_killed}')



# 실행결과(메모리:57,196 kb, 시간:157 ms)
