import sys

sys.stdin = open("_괄호짝짓기.txt")

for T in range(1, 11):
    matrix_ = []
    N = int(input())
    M = list(str(input()))
    count_1 = 0
    total_1 = 0
    count_2 = 0
    total_2 = 0
    count_3 = 0
    total_3 = 0
    count_4 = 0
    total_4 = 0
    for i in range(N):
        if M[i] == '(':
            count_1 += 1
        elif M[i] == ')':
            total_1 += 1
        elif M[i] == '{':
            count_2 += 1
        elif M[i] == '}':
            total_2 += 1
        elif M[i] == '[':
            count_3 += 1
        elif M[i] == ']':
            total_3 += 1
        elif M[i] == '<':
            count_4 += 1
        elif M[i] == '>':
            total_4 += 1
    if count_1 + count_2 + count_3 + count_4 != total_1 + total_2 + total_3 + total_4:
        print(f'#{T}', 0)
    elif count_1 + count_2 + count_3 + count_4 == total_1 + total_2 + total_3 + total_4:
        if (count_1 + total_1) % 2 == 0 and (count_2 + total_2) % 2 == 0 and (count_3 + total_3) % 2 == 0 and (count_4 + total_4) % 2 == 0:
            print(f'#{T}', 1)
        elif count_1 != total_1 or count_2 != total_2 or count_3 != total_3 or count_4 != total_4 :
            print(f'#{T}', 0)
    else:
        print(f'#{T}', 0)

            


