import sys

sys.stdin = open("_암호생성기.txt")

#테스트케이스는 10개
T = 10
#입력값 받아준다
for tc in range(1, T+1):
    N = int(input())
    number = list(map(int, input().split()))
    #1. 첫번째 숫자를 감소시키기 위해 2.한 사이클을 세기 위해서 
    count = 1
    # 5번 이동했으면 한 싸이클이 끝난다
    while count < 6:
        #처음에 맨 앞의 자리에 -1 한 값을 빼준다.
        queue = number.pop(0) - count
        # 만약에 queue값이 1보다 작으면 0으로 유지시키고 값을 넣어줘야한다.
        if queue < 0:
            queue = 0
        number.append(queue)

        #문제 조건에서 0보다 작아지는 경우 프로그램을 종료해야한다고 했으니 0이 되면 break
        if queue <= 0:
            break
        count += 1
        #만약에 count가 5를 넘으면 안 되고 하나의 싸이클이 끝났으니 count를 다시 1로 설정해준다.
        if count > 5:
            count = 1

    print(f"#{tc}", *number)