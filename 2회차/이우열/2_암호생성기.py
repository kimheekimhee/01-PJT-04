from collections import deque
import sys

sys.stdin = open("_암호생성기.txt")

for _ in range(10):
    n = int(input())
    pw = deque(list(map(int, input().split())))

    cnt = 1                                     # 1부터 빼야하므로 cnt를 1로 선언
    while True:
        if cnt == 6:                            # 5까지 빼야 하기 때문에 6이 되면 1로 초기화
            cnt = 1

        temp = pw.popleft()                     # 맨 앞에 있는 수를 뽑아서 temp에 저장
        if temp - cnt > 0:                      # temp - cnt가 0보다 크다면
            pw.append(temp - cnt)               # 뒤에 저장
        else:                                   # temp - cnt가 0보다 작거나 같으면
            pw.append(0)                        # 뒤에 0을 저장
            break                               # 0보다 작거나 같으면 프로그램 종료

        cnt += 1                                # 빼야할 수를 1씩 증가시켜준다

    print(f'#{n}', end=' ')
    print(*pw)
