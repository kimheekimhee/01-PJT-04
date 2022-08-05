# D3문제-암호생성기



# 입력
'''
1. 테스트 케이스의 번호 t
2. 8개의 정수
'''



# 출력
'''
1. #{해당 테스트케이스} + {마지막 암호 배열}
- 마지막 암호 배열은 한자리 수로 구성됨 
< 암호 생성 과정>
1) 8개의 숫자를 입력받음
2) 첫번째 숫자를 1 감소한 뒤, 맨 뒤로 보냄
2) 두번째 숫자를 2 감소한 뒤, 맨 뒤로 보냄 
3) 세번째 숫자를 3 감소한 뒤, 맨 뒤로 보냄 
4) 네번째 숫자를 4 감소한 뒤, 맨 뒤로 보냄 
5) 다섯번째 숫자를 5 감소한 뒤, 맨 뒤로 보냄 
<!------한사이클--------->
7) 사이클 반복
8) 숫자를 감소할 때 0보다 작아지는 경우, 0으로 유지되며 프로그램이 종료됨
'''



# 코드 2 접근방법
'''
<사이클 40번 돌때마다 8개 숫자는 각각 75씩 값이 감소>
1. 사이클 40번: 8개 숫자 x 5칸 이동
- 원형 큐라고 생각했을때 start 위치에 1번이 다시 돌아오려면 8 x 5 = 40번의 사이클이 돌아야함
2. 75씩 감소: (1+2+3+4+5) x 8
- 한 숫자당 (-1, -2, -3, -4, -5) 연산을 총 8번 진행하므로 (1+2+3+4+5) x 8 = 75씩 감소
'''



# 코드 1
import sys
from collections import deque

sys.stdin = open("input_text/_암호생성기.txt")

input_val = sys.stdin.read().split('\n')
idx = 0
while idx < len(input_val):
    # 각 테스트 케이스에 해당하는 8개의 숫자 가져오기
    test_case = input_val[idx]
    nums = deque(input_val[idx + 1].split())
    
    # 프로그램이 종료될 때까지 반복해서 사이클 돌기
    program_close = False
    while True:
        # 한 사이클 돌기
        for cnt in range(1, 5 + 1):
            front = nums.popleft()   # 맨 앞 수 가져오기
            if int(front) - cnt <= 0:
                nums.append(0)
                program_close = True
                break
            nums.append(int(front) - cnt)   # 맨 뒤로 보내기
        
        # 프로그램 종료 조건
        if program_close:
            break

    # 8자리 암호 배열 출력        
    print(f'#{test_case}', *nums)

    idx += 2

    

# 실행결과(메모리:64,256 kb, 시간:197 ms)



# 코드 2
import sys
from collections import deque

sys.stdin = open("input_text/_암호생성기.txt")

input_val = sys.stdin.read().split('\n')
idx = 0
while idx < len(input_val):
    # 각 테스트 케이스에 해당하는 8개의 숫자 가져오기
    test_case = input_val[idx]
    nums = list(map(int, input_val[idx + 1].split()))

    # 사이클 40번 돌때마다 8개 숫자는 각각 75씩 값이 감소
    # 따라서, 처음부터 사이클을 반복할 필요 없음
    nums_after_cycles = deque()
    for num in nums:
        nums_after_cycles.append(num - min(nums) // 75 * 75)

    # 현재 숫자 배열이 프로그램 종료 조건에 해당되는지 확인
    program_close = False
    if 0 in nums_after_cycles:
        program_close = True

    # 프로그램이 종료될 때까지 반복해서 사이클 돌기
    while True:
        # 프로그램 종료 조건
        if program_close:
            break

        # 한 사이클 돌기
        for cnt in range(1, 5 + 1):
            front = nums_after_cycles.popleft()   # 맨 앞 수 가져오기
            if int(front) - cnt <= 0:
                nums_after_cycles.append(0)
                program_close = True
                break
            nums_after_cycles.append(int(front) - cnt)   # 맨 뒤로 보내기
        
    # 8자리 암호 배열 출력        
    print(f'#{test_case}', *nums_after_cycles)

    idx += 2

    

# 실행결과(메모리:60,100 kb, 시간:167 ms)