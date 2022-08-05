import sys

sys.stdin = open("_암호생성기.txt")

for test_case in range(10):                     # 10개의 테스트케이스
    T = int(input())                            # 현재 테스트케이스
    code = list(map(int, input().split()))      # 8자리 암호 리스트

    while True:                                 # 사이클 반복
        for minus in range(1, 6):               # 1사이클 당 5회 감소, 이동
            code.append(code.pop(0) - minus)    # 첫 번째 숫자 감소, 맨 뒤로
            if code[-1] <= 0:                   # 마지막 숫자가 0보다 이하이면
                code[-1] = 0                    # 마지막 숫자를 0으로
                break                           # 사이클 종료
        if code[-1] == 0:                       # 마지막 숫자가 0이면
            break                               # 암호 생성 종료
    
    print(f'#{T}', *code)                       # 최종 8자리 암호 출력