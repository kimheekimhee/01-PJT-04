import sys
import heapq
sys.stdin = open("_암호생성기.txt")

for test_case in range(10):
    T = int(input())
    list_ = list(map(int, input().split()))
    # 맨 마지막이 0이 되면 바로 종료하게 설정
    while list_[-1] != 0:
        for i in range(1, 6):
            # 문제에서는 1 감소 후 맨 뒤로 이동이지만, 0보다 작을 경우에도 일단 0으로 두고 맨 뒤로 이동시킨 다음 종료
            # 0보다 작을 경우 비교하고 종료시키는 것 보다 일단 pop후 맨 뒤에 넣는 것이 더 일찍 이루어져야한다고 생각
            x = list_.pop(0)
            list_.append(x)
            list_[-1] -= i
            if list_[-1] <= 0:
                list_[-1] = 0
                break
    print(f'#{test_case + 1}', end = ' ')
    for i in list_:
        print(i, end = ' ')
    print()