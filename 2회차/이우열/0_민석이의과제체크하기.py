import sys

sys.stdin = open("_민석이의과제체크하기.txt")

t = int(input())

for i in range(1, t + 1):
    n, k = map(int, input().split())

    submit = list(map(int, input().split()))    # 과제를 제출한 사람을 리스트에 저장
    result = [0] * (n + 1)                      # 과제의 결과를 저장하기 위한 리스트 선언

    for j in submit:                            # 과제를 제출한 사람이라면
        result[j] = 1                           # 결과 리스트에 1을 추가

    print(f'#{i}', end=' ')
    for j in range(1, n + 1):
        if result[j] == 0:                      # 결과에 0이라면 과제 제출을 하지 않음
            print(j, end=' ')                   # 인덱스 출력
    print()
