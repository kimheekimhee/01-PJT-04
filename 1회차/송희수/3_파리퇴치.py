import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split(' '))
    matrix = [list(map(int, input().split())) for a in range(N)]
    # 각 리스트의 서로 연속하는 숫자 두개여야하고 다음 행과 붙어 있어야한다. 결론적으로 행으로 1, 열로 1씩차이나느 것들의 모임이다.
    # 이 요소들의 합이 제일 큰 값을 구해야한다.
    # 결론 MXM행렬을 다구하고 거기서 최대 값을 도출하면된다.
    