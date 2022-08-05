import sys

sys.stdin = open("_파리퇴치.txt")

# 2차원 리스트 안에 파리의 수의 합을 구해주는 함수
def hap(lst):
    f_sum = 0
    for i in lst:
        f_sum += sum(i)
    return f_sum
for test_case in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    # m * m 크기로 전 구간을 다 돌기 위한 반복문 및 함수 사용
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            answer = max(answer, hap([fly[i + x][j:j + m] for x in range(m)]))
    print(f"#{test_case} {answer}")