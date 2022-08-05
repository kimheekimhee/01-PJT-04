from collections import deque

for _ in range(10):
    test_case = int(input())
    list_ = list(map(int, input().split()))

    deque_ = deque(list_)
    #print(deque_)
    is_done = True

    while is_done :
        for i in range(1,6):
            a = deque_.popleft()
            if a - i > 0:
                deque_.append(a-i)
            if a - i <= 0 :
                deque_.append(0)
                is_done = False
                break

    #print(deque_)

    print(f'#{test_case}', end=' ')
    for elem in deque_:
        print(elem, end=' ')
    print()