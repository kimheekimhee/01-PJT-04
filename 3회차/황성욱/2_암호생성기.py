import sys

sys.stdin = open("_암호생성기.txt")
cnt = 0
while cnt < 10:
    n = int(input())
    stk = list(map(int, input().split()))

    is_break = True 
    while is_break:
        for i in range(5): # 1사이클 1 ~ 5를 빼줌
            if stk[0] - (i + 1) > 0: # 사이클에서 1 ~ 5를 빼준 값이 0 보다 클 때
                stk[0] -= (i + 1)
                stk.append(stk[0])
                stk.pop(0)
            
            elif stk[0] - (i + 1) <= 0: # 사이클에서 1 ~ 5를 빼준 값이 0보다 작을 때
                stk[0] = 0 # 불필요한 코드
                stk.append(stk[0]) # stk.append(0)
                stk.pop(0)
                is_break = False
                break
    print(f'#{n} {" ".join(map(str, stk))}')
    cnt += 1