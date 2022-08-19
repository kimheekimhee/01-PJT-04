# D3문제-민석이의 과제 체크하기



# 입력
'''
1. 테스트 케이스 수 T
2. 수강생 수 N, 과제를 제출한 사람의 수 K
- 2 <= N <= 100
- 1 <= K <= N
3. 과제를 제출한 사람의 번호 K개
- 1 <= 번호 <= N
'''



# 출력
'''
1. #{해당 테스트케이스} + {과제를 제출하지 않은 사람의 번호(오름차순)} 
'''



# 코드 1
import sys

sys.stdin = open("input_text/_민석이의과제체크하기.txt")

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    done_people = map(int, input().split())   # 과제를 제출한 사람
    
    # 과제를 제출한 사람 체크
    check = [False] * (N + 1)  
    for person in done_people:
        check[person] = True

    # 과제를 제출하지 않은 사람 출력
    print(f'#{test_case}', end=' ')
    for i in range(1, N + 1):
        if not check[i]:
            print(i, end=' ')
    print()



# 실행결과(메모리:64,052KB, 시간:356ms)



# 코드 2
import sys

sys.stdin = open("input_text/_민석이의과제체크하기.txt")

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    done_people = set(map(int, input().split()))   # 과제를 제출한 사람

    # 과제를 제출하지 않은 사람 출력
    print(f'#{test_case}', end=' ')
    for num in range(1, N + 1):
        if num not in done_people:
            print(num, end=' ')
    print()



# 실행결과(메모리:64,082KB, 시간:444ms)