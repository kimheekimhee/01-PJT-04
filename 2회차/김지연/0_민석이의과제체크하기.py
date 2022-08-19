import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input()) # 테스트케이스

for tc in range(1, T+1):
    N, K = map(int, (input().split())) # 전체 수강생, 제출한 수강생의 수
    n = list(map(int, input().split())) # 제출한 수강생의 번호
    result = []

    for i in range(1, N+1):
        if i not in n:
            result.append(i)

    print(f'#{tc}', *result)