import sys

sys.stdin = open("_민석이의과제체크하기.txt")

"""

"""

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    # 학생 리스트 목록
    work_list = list(range(1, N + 1))
    done_list = list(map(int, input().split()))
    n_done_list = []
    for number in range(1, N + 1):
        if number not in done_list:
            n_done_list.append(number)
    answer = ''
    for elem in n_done_list:
        answer += str(elem) + ' '
    print(f'#{t} {answer}')