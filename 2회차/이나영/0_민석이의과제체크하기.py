import sys

sys.stdin = open("_민석이의과제체크하기.txt")

t = int(input())

for _ in range(1, t+1):
    N, K = map(int, input().split())
    # N : 수강생 수, K : 제출인원
    hw_completed = map(int, input().split())
    # 제출한 사람의 번호
    not_completed = 0 
    # 제출하지 않은 사람의 변수
    # 
    for i in range(1, N+1, +1):
        if i not in hw_completed:
            not_completed.append(i) #보면 append하는걸 외운것같음. 큰 흐름은 익혔는데 코드리뷰 하려고 러버덕에게 말해보니 완벽히 안됐음.

print('#t', not_completed)
#역시나 오류뜸
