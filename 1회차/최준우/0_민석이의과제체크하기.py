import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

for test_case in range(T):
    N, K = map(int, input().split()) # N: 수강생 수, K: 제출한 사람 수
    submitted = list(map(int, input().split())) # 제출한 수강생 번호
    result = [] # 제출하지않은 번호 리스트

    for i in range(1, N+1): # N번을 순회하면서 
        if i not in submitted: # 해당하는 반호가 제출하지않은 번호면
            result.append(i) # 제출하지않은 번호 리스트에 추가한다.
    
    print(f'#{test_case + 1}', end = ' ') # 출력부분
    for i in result:
        print(i, end = ' ')
    print()