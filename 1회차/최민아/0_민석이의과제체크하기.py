import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())                                # 테스트케이스 개수

for test_case in range(1, T+1):
    N, K = map(int, input().split())            # 수강생 수, 과제 제출 수
    submit = list(map(int, input().split()))    # 제출자 번호

    no_submit = []                              # 미제출자 리스트
    for i in range(1, N+1):                     # 1~N번 중에서
        if i not in submit:                     # 제출자 번호에 없으면
            no_submit.append(i)                 # 미제출자 번호 추가

    print(f'#{test_case}', *no_submit)          # 미제출자 번호 출력