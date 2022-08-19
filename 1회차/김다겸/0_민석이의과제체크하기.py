# import sys
# sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

for t in range(1, T+1):
    # input 값 받기
    n, k = map(int, input().split())
    assign = list(map(int, input().split()))
    # students 리스트 생성
    students = []

    # 1부터 n까지 students에 추가하기
    for i in range(1, n+1):
        students.append(i)

    # 입력받은 assign에 순회
    for i in range(len(assign)):
        # 만약 assign[i]가 students에 있다면
        if assign[i] in students:
            # students에서 해당 값 삭제
            students.remove(assign[i])
    print(f'#{t}', end=' ')

    for i in students:
        print(i, end=' ')
    print()