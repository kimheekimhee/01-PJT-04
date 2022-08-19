import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    students = list(map(int,input().split()))
    result =[]

    # 1에서 N까지의 숫자가 students 배열에 없으면 문제를 안 푼 사람이므로
    # result에 넣어줍니다.
    for i in range(1, N+1):
        if i not in students:
            result.append(i)
    
    print(f'#{tc}', *result )