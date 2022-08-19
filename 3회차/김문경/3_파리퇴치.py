import sys
from pprint import pprint

sys.stdin = open("_파리퇴치.txt")

T = int(input())

for test_case in range(T):
    N, M = map(int, input().split())
    flylist = []
    for i in range(N):
        flylist.append(list(map(int, input().split())))
    # M 크기에 있는 파리 개수 넣는 리스트
    scorelist = []

    # i, j는 시작하는 위치의 x, y 좌표값
    # M x M의 파리채의 왼쪽 위 꼭짓점이라고 생각
    # N과 M의 관계를 계산해보면 N - M + 1 번씩 반복을 돌아야함 
    for i in range(N - M + 1):
        for j in range(N - M + 1): 
            result = 0
            # 파리채의 각 변의 길이가 M이므로 왼쪽위 꼭짓점 (i, j)을 기준으로
            # 가로로 M, 세로로 M만큼의 칸 하나하나씩 돌면서 값을 result에 저장 
            for row in range(i, i + M):
                for col in range(j, j + M):
                    result += flylist[row][col]
            scorelist.append(result)
            # print(scorelist)
    print(f'#{test_case + 1}', max(scorelist))

