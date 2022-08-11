import sys
from collections import deque

sys.stdin = open("_암호생성기.txt")

# 피드 받고 추가
for _ in range(10):
    cycle = [1, 2, 3, 4, 5]
    test = int(input())
    numbers = deque(list(map(int, input().split())))

    cnt = 0
    while numbers[-1] > 0:
        x = numbers.popleft()
        x -= cycle[cnt]
        cnt += 1
        cnt %= 5
        numbers.append(x)
    numbers[-1] = 0
    print(f'#{test}', end = ' ')
    for i in numbers:
        print(i, end = ' ')
    print()







# 나의 풀이
# for _ in range(10):
#     cycle = [1, 2, 3, 4, 5]
#     # 사이클은 [1, 2, 3, 4, 5]를 순회합니다
#     test = int(input())
#     numbers = list(map(int, input().split()))
#     cnt = 0
#     # 계산이 몇 번이 진행되었는지 확인해줄 값을 변수에 저장해줍니다.
#     while numbers[-1] > 0:
#         # 마지막 값이 0보다 작을때까지 계속 합니다
#         numbers[0] -= cycle[cnt % 5]
#         # 첫 자리 값이 사이클을 반복하며 줄어들것이기 때문에 0 인덱스 값을 빼줍니다.
#         # cnt % 5를 해주고 이 반복에서 cnt를 매번 1씩 증가해주면 5회를 주기로 반복하는 사이클을 설정 가능합니다.
#         cnt += 1
#         numbers = numbers[1::] + [numbers[0]]
#         # numbers를 슬라이싱하여 1번 인덱스 값부터의 리스트 뒤에 0번 인덱스 값을 리스트화 시킨값을 더해줍니다.
#     numbers[-1] = 0
#     # 이 과정이 끝나면 마지막 자리가 음수가 되는 경우에도 0으로 출력시켜 준다고 했기 때문에 값을 0으로 바꾸어 줍니다.
#     print(f'#{test}', end = ' ')
#     for i in numbers:
#         print(i, end = ' ')
#     print()