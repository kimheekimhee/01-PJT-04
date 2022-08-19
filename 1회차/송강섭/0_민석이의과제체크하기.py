import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())
for test_case in range(1, T+1):
    # n = 수강생 수
    # m = 제출한 수강생 수
    n, m = map(int, input().split())
    # 제출한 수강생번호를 리스트에 담아줌
    k = list(map(int, input().split()))
    # 빈 리스트를 만들어 append해줄거임
    arr = []

    # 학생 수 만큼 반복문 돌려주고
    for i in range(1, n+1):
        # 학생이 제출한 수강생안에 있는지 확인 후 없으면 빈 리스트에 담아줌
        if i not in k:
            arr.append(i)
        # 자동정렬 해주고
        arr.sort()
    # #테스트케이스를 미리 end=" "로 땡겨와줌
    print(f'#{test_case}', end=' ')
    # 이대로 출력하면 리스트로 출력되니까 for문으로 돌려준다음에 테스트케이스처럼 end로 잡아줌
    for j in arr:
        print(j, end=' ')
    # 한번에 출력해줌
    print()