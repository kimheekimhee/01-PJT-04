from collections import deque

# deque를 활용하여 쉽게 풀 수 있는 문제
# 문제 조건에 테스트 케이스 수가 없어서 input을 보고 직접 확인했습니다.

for _ in range(10):
    test_case = int(input())
    list_ = list(map(int, input().split()))
    
    # list를 deque로 바꾸고
    deque_ = deque(list_)

    # while문을 빠져나올 조건 생성
    is_done = True

    while is_done :
        # 1~5번씩 숫자를 빼기 위한 for문
        for i in range(1,6):

            # 제일 왼쪽 값을 구한 뒤
            a = deque_.popleft()

            # 1~5중 차례에 해당하는 값을 뺐을 때 0보다 크면 끝에 다시 추가
            if a - i > 0:
                deque_.append(a-i)

            # 1~5중 차례에 해당하는 값을 뺐을 때 0보다 작거나 같으면 끝에 추가후 for문 과 while문 종료
            if a - i <= 0 :
                deque_.append(0)
                is_done = False
                break

    # 결과 출력
    print(f'#{test_case}', end=' ')
    for elem in deque_:
        print(elem, end=' ')
    print()