import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    students = list(map(int, input().split())) # 과제 낸 사람
    list_ = [] # 과제 안 낸 사람
    for i in range(1, n + 1): # 1~n
        if i not in students: # 안낸사람 번호를
            list_.append(i) # 리스트에 추가
    print(f'#{test_case}', *list_) # 껍데기 벗겨서 출력