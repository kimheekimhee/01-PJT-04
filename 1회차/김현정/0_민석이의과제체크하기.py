import sys
from winreg import REG_RESOURCE_LIST

sys.stdin = open("_민석이의과제체크하기.txt")

# 결과값 담을 리스트 선언
result = []

# 테스트케이스 수 변수 선언
T = int(input())

# T 갯수만큼의 테스트케이스 처리
for i in range (T):
    # 테스트케이스 담을 변수 N(수강생 수), C(과제 제출 수강생 수) 선언
    N, C = map(int, input().split())

    # 과제 제출한 사람 번호 리스트 선언
    K_list = list(map(int, input().split()))

    # 테스트케이스 별 미제출 수강생 번호 담는 리스트 선언
    result_tmp = []

    # 수강생 수만큼 for문 구동하고 제출 리스트에 없으면 결과값에 입력
    for j in range(1, N+1):
        if j not in K_list:
            result_tmp.append(j)
    
    # 오름차순 정렬
    result_tmp.sort()

    # 테스트케이스에 따른 미제출 수강생 리스트를 결과값에 담음
    result.append(result_tmp)

# 결과 출력
for h in range(1, T+1):
    print(f"#{h}", end=' ')
    for k in result[h-1]:
        print(k, end=' ')
    print("")