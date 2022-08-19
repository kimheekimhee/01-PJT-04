# Solving Club 2주차 모의고사

""" 
N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.
M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.
죽은 파리의 개수를 구하라!

# 입력
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
다음 N 줄에 걸쳐 N x N 배열이 주어진다.

10
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3

# 출력
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력

# 접근 방법
1. 이중리스트를 순회하는 이중리스트를 만들어 순회한다.
2. 이중리스트가 순회하는 범위는 주어진 배열의 범위를 벗어나선 안 된다.

"""
from calendar import c
import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())
for t in range(1, T+1):
        
        N, M = map(int, input().split())
        matrix = [list(map(int, input().split())) for _ in range(N)]
        max_sum = 0
        # 이중리스트 순회할 반복문
        # M 만큼의 범위를 제외하고 순회한다.
        for r in range(N - M+1):
                for c in range(N - M+1):
                        # 행 순회가 끝나면 파리채의 합 초기화
                        sum_arry = 0
                        for i in range(r, r + M):
                                for j in range(c, c + M):
                                        # 탐색할 i, j 는 리스트의 범위를 벗어나면 안 된다.
                                        if 0 <= i <= N-1 and 0 <= j <= N-1:
                                                sum_arry += matrix[i][j]
                        if max_sum < sum_arry:
                                max_sum = sum_arry
        print(f'#{t} {max_sum}')