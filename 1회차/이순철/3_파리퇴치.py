from pprint import pprint
import sys

sys.stdin = open("_파리퇴치.txt")

# 행렬값은 n*n 채 m*m
# 행렬 칸 마다 숫자 있고 채에 해당하는 4칸의 숫자 합이 가장 큰 경우 출력
# 5<=n<=15 /  2<=m<=n   /  칸의 숫자<=30

t = int(input())
for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    pan = [list(map(int, input().split())) for _ in range(n)]
    # pprint(pan)
    
    cnt = 0
    for x in range(n - m):
        for y in range(n - m):
            