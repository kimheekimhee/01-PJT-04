import sys

sys.stdin = open("_괄호짝짓기.txt")

T = 10
for tc in range(1, T + 1):
    N  = int(input())
    text = list(map(str, input()))
    check_1 = ['{','[','(','<']
    check_2 = ['}',']',')','>']
    check_li = []
    for j in text:
        if j in check_1:
            check_li.append(j)
             
        else:
            if check_1[check_2.index(j)] == check_li[-1]:
                check_li.pop(-1)
            else:
                break

    if len(check_li) == 0:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
        


