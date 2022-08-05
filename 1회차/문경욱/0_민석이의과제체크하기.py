# import sys

# sys.stdin = open("_민석이의과제체크하기.txt")

# set()을 활용하여 전체 사람 set - 낸 사람 set을 하면 과제를 내지 않은 사람들의 set을 구할 수 있다.

T = int(input())
for test_case in range(1, T+1):
    a, b = map(int, input().split())
    
    # 처음부터 total을 set으로 선언한 뒤 add로 할 수 있지만, 리스트를 set으로 변환하는 것을 이용
    # 전체 사람용 set 생성
    total_ = []
    for i in range(1,a+1):
        total_.append(i)
    total_ = set(total_)

    # 낸 사람용 set 생성
    handin_ = list(map(int, input().split()))
    handin_ = set(handin_)

    # 전체에서 안 낸 사람 제거
    no_handin_ = total_ - handin_
    
    # 하나씩 출력
    print(f'#{test_case}', end= ' ')
    for elem in no_handin_:
        print(elem, end=' ')
    print()