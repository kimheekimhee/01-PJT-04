# N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수 의미
# M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 함
# 죽은 파리의 개수를 구하라

# 첫 줄에는 테스트 케이스의 개수 T가 주어지고
# 각 테스트 케이스의 첫 번째 줄에 N과 M이 주어진다
# 다음 N줄에 걸쳐 N x M 배열이 주어진다

# 출력 예시
#1 49
#2 159
#3 428
#4 620
#5 479
#6 941
#7 171
#8 968
#9 209
#10 1242

import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    N = m - 1
    max_v = 0
    
    # N - M + 1 범위의 idx만큼 순회
    for i in range(n - N):
        for j in range(n - N):
            sum_v = 0
            # 해당 인덱스에서 M * M 범위 내 원소합 저장
            for di in range(m):
                for dj in range(m):
                    sum_v += board[i + di][j + dj]
            # 최대값과 비교하며 최대값 저장
            if sum_v > max_v:
                max_v = sum_v
    print('#{} {}'.format(tc, max_v))