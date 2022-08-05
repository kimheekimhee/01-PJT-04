# 민석이는 제출한 사람의 목록을 받았다.
# 수강생들은 1번에서 N번까지 번호가 매겨져 있고, 어떤 번호의 사람이 제출했는지에 대한 목록을 받은 것이다.
# 과제를 제출하지 않은 사람의 번호를 오름차순으로 출력하는 프로그램을 작성하라.


# [출력]
# 각 테스트 케이스마다 과제를 제출하지 않은 사람의 번호를 오름차순으로 출력한다.


# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
T = int(input())

for t in range(1, T+1):
    # 수강생의 수 N, 과제를 제출한 사람의 수 K가 공백으로 구분되어~
    N, K = map(int, input().split())

    # 두 번째 줄에는 과제를 제출한 사람의 번호 K개가 공백으로 구분되어~
    # 번호는 1이상 N이하의 정수이며 같은 번호가 두 번 이상 주어지는 경우는 없다.
    submission_n = list(map(int, input().split()))
    res = []

    for n in range(1, N+1):
        if n not in submission_n:
            res.append(n)

    res.sort()
    print(f'#{t}', *res)