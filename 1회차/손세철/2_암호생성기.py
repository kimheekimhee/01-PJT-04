import sys

sys.stdin = open("_암호생성기.txt")
# 한 사이클 1~5
# 맨앞에  숫자 꺼내서 숫자 감소  후 제일 뒤에 넣는다.
# 0보다 작으면 0으로하고 break

T=10
for i in range (1,T+1):
    input()
    #암호 
    password = list(map(int, input().split()))
    count = 1

    while True:
        a = password.pop(0) - count
        # -되면 0
        if a < 0 : a = 0
        password.append(a)
        # 0이되면 암호로 적용 break
        if a == 0: break
        count += 1
            # 1사이클당 5번
        if count > 5 : count = 1
    print('#{} '.format(i), end='')
    print(*password)