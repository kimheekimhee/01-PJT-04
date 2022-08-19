import sys

sys.stdin = open("_민석이의과제체크하기.txt")

for test_case in range(1, int(input()) + 1):
    # n명 수강생 , 과제 완료한 k명
    n, k = map(int,input().split())

    # 과제 완료한 k명의 번호
    homework = list(map(int, input().split()))
    # 정답을 넣을 리스트
    answer = []
    # 과제 완료한 k명의 번호에 포함 되지 않는지 판단
    # 오름차순으로 정렬 하라 하였기 때문에 1 ~ n + 1 으로 돌림
    for i in range(1, n + 1):
        if i not in homework:
            #과제 안한 인원
            answer.append(i)
    print(f"#{test_case} {' '.join(map(str,answer))}")