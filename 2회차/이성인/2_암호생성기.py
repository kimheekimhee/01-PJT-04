import sys
from collections import deque
sys.stdin = open("_암호생성기.txt")


for t in range(1,11): # 
    _ = input()
    data = list(map(int, input().split())) 
    data_queue = deque(data) # popleft쓸려고 deque를 가져왔습니다. 
    i = 0
    while True:
        i += 1
        a = data_queue.popleft() # 앞에거 빼고
        a -= i # 빼는 값 1씩 증가 
        if i == 5: # 5개 되면 리셋
            i = 0
        if a <= 0: # 빼는 값이 0이하가 되면 0으로 만들어 주고 붙인다. 그리고 멈춘다. 
            a = 0
            data_queue.append(a)
            break
        data_queue.append(a)
    print(f"#{t}", end=" ")
    print(*(data_queue))
        


