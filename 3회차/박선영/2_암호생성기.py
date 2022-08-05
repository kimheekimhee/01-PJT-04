import sys

sys.stdin = open("_암호생성기.txt")

test_case = 0
while 1:
    try:
        T = int(input())
    except EOFError:
        break
    test_case += 1

    numbers = list(map(int, input().split()))
    while 1:
        for i in range(1, 6):               
            if numbers[0]-i <= 0:             # -1 없이 0을 뒤로 보내고 break
                numbers.pop(0)                # 큐 이용해서 앞에 빼고 뒤에 붙임
                numbers.append(0)
                break
            else:
                numbers.append(numbers.pop(0)-i)

        if numbers[-1] == 0:
            break
    print(*numbers)

    print(f'#{test_case}', *numbers)

