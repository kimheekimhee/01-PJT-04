import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")
T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    answer = 0

    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i][j] == 0:
                if count == k:
                    answer += 1
                count = 0
                continue
            count += 1
        if count == k:
            answer += 1

    for i in range(n):
        count = 0
        for j in range(n):
            if arr[j][i] == 0:
                if count == k:
                    answer += 1
                count = 0
                continue
            count += 1

        if count == k:
            answer += 1

    print(f'#{test_case} {answer}')

