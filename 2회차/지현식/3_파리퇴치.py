import sys

sys.stdin = open("_파리퇴치.txt")

def hap(lst):
    f_sum = 0
    for i in lst:
        f_sum += sum(i)
    return f_sum
for test_case in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            answer = max(answer, hap([fly[i + x][j:j + m] for x in range(m)]))
    print(f"#{test_case} {answer}")