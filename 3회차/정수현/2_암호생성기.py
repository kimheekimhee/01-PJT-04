import sys

sys.stdin = open("_암호생성기.txt")

for t in range(1, 11):
    input()
    password = list(map(int, input().split()))
    i = 1
    while 1:
        head = password.pop(0) -i
        if head <= 0:
            password.append(0)
            break
        password.append(head)
        # 감소치 사이클 1 ~ 5
        i += 1
        if i > 5:
            i=1
    print(f'#{t}',*password)