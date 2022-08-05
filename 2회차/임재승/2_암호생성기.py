import sys

sys.stdin = open("_암호생성기.txt")

from collections import deque

for _ in range(1, 11):
    T = int(input())
    li = list(map(int, input().split()))
    # 받아온 리스트 li를 deque로 선언해준다.
    ing = deque(li)
    # while문으로 ing의 마지막값이 0이 아니라면 계속해서 돌아가게해준다.
    while ing[7] !=0 :
        # 조건에 맞게 1이상 6미만으로 for문을 계속해서 돌려준다
        for i in range(1, 6):
            # ing[0]을 빼주면서 temp라는 임시값에 넣어주고
            temp = ing.popleft()
            # 빼온 값이 0보다 작으면 0으로 지정해주고 가장 우측값으로 전달
            if temp - i <= 0:
                temp = 0
                ing.append(temp)
                break
            # 아니라면 빼준값을 가장 우측값으로 전달
            else:
                temp -= i
                ing.append(temp)
    print(f'#{T}', end=' ')
    print(*ing)
        