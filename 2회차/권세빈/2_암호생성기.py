import sys
sys.stdin = open("_암호생성기.txt")

from collections import deque

T = 10
for tc in range(1, T+1):
    t = int(input())
    n = list(map(int,input().split()))
    n = deque(n)

    # 마지막이 0이 되면 종료
    while n[-1] != 0:
        # 한 사이클 돌리기
        for i in range(1,6):
            # 뺐을 때 0보다 크면
            if n[0] - i > 0:
                # 왼쪽에서 뺀 다음 오른쪽에 추가
                n[0] -= i
                n.append(n.popleft())

            # 뺐을 때 0보다 작으면
            elif n[0] - i <= 0:
                # 0으로 바꾸고
                n[0] = 0
                # 왼쪽에서 뺀 다음 오른쪽에 추가
                n.append(n.popleft())
                break
            
    print(f'#{t}',*n)
