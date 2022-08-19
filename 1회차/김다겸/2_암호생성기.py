from collections import deque
# import sys

# sys.stdin = open("_암호생성기.txt")

for tc in range(1, 11):
    t = int(input())
    # deque로 입력받기
    num = deque(map(int, input().split()))
    # 진행 가능
    flag = True

    # 계속 진행 가능하면
    while flag:
        # 1부터 5번 반복
        for i in range(1, 6):
            # 만약 num의 마지막 수가 0보다 작거나 같으면
            if num[-1] <= 0:
                # 진행 불가능으로 저장
                flag = False
                # 반복문 빠져나가기
                break
            # 첫번째 값 pop
            pop_num = num.popleft()
            # pop_num에서 1부터 차례대로 뺀 수가 0보다 작으면
            if pop_num - i <= 0:
                # num 맨 뒤에 0 추가
                num.append(0)
            # 0보다 크거나 같으면
            else:
                # num에 pop_num에서 1부터 차례대로 뺀 수 추가
                num.append(pop_num-i)

    print(f'#{t}', end=' ')

    for i in list(num):
        print(i, end=' ')
    print()