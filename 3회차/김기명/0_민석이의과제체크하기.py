# import sys

# sys.stdin = open("_민석이의과제체크하기.txt")

# N명. 제출안한사람 번호출력.

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split()) # N 수강생 K 제출자 수
    list_K = list(map(int, input().split())) # 제출자들의 번호 리스트.
    print(f'#{test_case}', end = ' ')
    for i in range(1, N + 1):
        if i not in list_K:
            print(i, end = ' ')
        if i == N:
            print()
            