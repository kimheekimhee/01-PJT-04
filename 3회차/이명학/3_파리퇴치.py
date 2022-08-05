from pprint import pprint
import sys

sys.stdin = open(
    "C:\\Users\\이명학\\Desktop\\멀티캠퍼스\\01-PJT-04\\3회차\\이명학\\_파리퇴치.txt")

T = int(input())
# arr =[[1, 3, 3, 6, 7],
#       [8, 13, 9, 12, 8],
#       [4, 16, 11, 12, 6],
#       [2, 4, 1, 23, 2],
#       [9, 13, 4, 7, 3]]
for _ in range(1, T+1):
    result = 0
    N, M = map(int, input().split())  # 정사각형 N과 파리채 크기 M
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N-M+1):
        for j in range(N-M+1):
            count = 0
            # range의 i와 j값을 index 범위가 넘어가지 않게끔 설정
            for a in range(i, i+M):  # 영역에 해당하는 파리 갯수
                for b in range(j, j+M):
                    count += arr[a][b]

            result = max(result, count)

    print(f"#{_}", result)
