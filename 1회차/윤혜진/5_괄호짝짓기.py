# D4-괄호 짝짓기



# 입력
'''
<총 10개의 테스트케이스>
1. 테스트 케이스당 괄호 문자열 길이
2. 괄호 문자열
'''



# 출력
'''
1. #{해당 테스트케이스} + {괄호 문자열의 유효성}
- 괄호 문자열이 유효하다면, 1 출력
- 괄호 문자열이 유효하지 않다면, 0 출력
'''


# 코드
import sys

sys.stdin = open("input_text/_괄호짝짓기.txt")

T = 10
for test_case in range(1, T + 1):
    length = int(input())
    ps = input()
    couple = {   # 괄호 쌍
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }

    # 유효한 괄호 문자열인지 확인
    stack = []
    possible = True   # 유효한 괄호 문자열인지
    idx = 0
    while idx == 0 or stack:
        p = ps[idx]   # 괄호
    
        # 닫힌 괄호인 경우
        if p in couple:
            if not stack or stack.pop() != couple[p]:
                possible = False
                break
        # 여는 괄호인 경우
        else:
            stack.append(p)

        idx += 1

    # 유효성에 따라 값 출력
    if possible and not stack:   # 유효함
        print(f'#{test_case} {1}')
    else:   # 유효하지 않음
        print(f'#{test_case} {0}')



# 실행시간(메모리:56,944 kb, 시간:143 ms)