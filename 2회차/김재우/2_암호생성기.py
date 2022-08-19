import sys

sys.stdin = open("_암호생성기.txt")

T = 10              

for tc in range(1, T+1):
    tc_list = input()
    num = list(map(int, input().split()))
    minus = 1                                    # 암호 숫자를 빼주기 위한 변수
    
    while True:                                 
        
        if minus > 5:                           # minus가 5보다 커지면
            minus = 1                           # 1로 초기화를 시켜준다. (문제 속 한 사이클에 의거)
        
        num.append(num.pop(0) - minus)          # 맨 앞에서 뺀(pop) 값을 num 맨 뒤에 넣어줄(append) 것이기 때문에 (pop - minus) > append

        if num[7] <= 0:                         # 요소는 8개로 정해져 있기 때문에 문제의 규칙인 마지막 값이 0이거나 그 아래가 된다면 반복문을 종료
            num[7] = 0                          # 하지만 음수가 되는 경우는 0으로 만들어준다!
            break

        minus += 1                              # 반복문을 돌면서 minus 는 1~5를 반복해야 하기 때문에 값을 증가시켜준다
    
    # 출력문 
    print(f'#{tc}', end =' ')                   # 급하게 출력하느라.. 리스트 푸는 방법이 생각이 안 났습니다.. 
    print(*num)                                 # 더 좋은 방법 피드백 받고싶어요!