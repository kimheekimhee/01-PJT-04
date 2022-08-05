import sys

sys.stdin = open("_암호생성기.txt")
T = 10
for i in range(1, T+1):
    case = int(input())
    number_list = list(map(int, input().split()))
    while number_list[7] != 0:
        for j in range(1, 6):
            number_list[0] -= j
            n1 = number_list.pop(0)
            if n1 < 0:
                n1 = 0
            number_list.append(n1)
            if number_list[7] == 0:
                print(f'#{i}', *number_list)
                break
        # if number_list[7] == 0:
        #     break