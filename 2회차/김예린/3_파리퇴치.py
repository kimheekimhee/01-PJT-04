import sys

t = int(input())
for test_case in range(1, t + 1):
    n, m = map(int, input().split())        # n == 배열, m == 파리채 면적 

    metrix = []
    sum_ = 0

    for _ in range(n):                      # 배열 만들기
        metrix.append(list(input().split()))

    for i in range(n):
        for j in range(m):
            while True: 
                if j + 1 == n:
                    sum_ = sum(metrix[i][j] + metrix[i + 1][j] + metrix[j][i] +  metrix[j+1][i])

                    print(sum_)
                                                # m x m에서 합산값이 제일 큰 값을 출력 == 순회

sys.stdin = open("_파리퇴치.txt")
