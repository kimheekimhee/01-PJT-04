import sys

sys.stdin = open("_괄호짝짓기.txt")

# 결과값 담을 리스트 선언
result = []

# 테스트케이스 10개 처리
for i in range (10):
    # 테스트케이스 길이 담을 변수 선언
    N = int(input())
    # 테스트케이스 문자열 담을 변수 선언
    test_case = input()

    # cnt1: () 괄호 처리 변수
    cnt1 = 0
    # cnt2: [] 괄호 처리 변수
    cnt2 = 0
    # cnt3: {} 괄호 처리 변수
    cnt3 = 0
    # cnt4: <> 괄호 처리 변수
    cnt4 = 0

    # 테스트케이스 문자열 처리
    for j in test_case:
        if j == "(":
            cnt1 += 1
        elif j == "[":
            cnt2 += 1
        elif j == "{":
            cnt3 += 1
        elif j == "<":
            cnt4 += 1
        elif j == ")":
            cnt1 -= 1
        elif j == "]":
            cnt2 -= 1
        elif j == "}":
            cnt3 -= 1
        elif j == ">":
            cnt4 -= 1
        
        # 만약 변수가 0보다 작다면, 여는 괄호보다 닫는 괄호가 많으므로 완전 괄호 성립X
        # for문을 더이상 돌릴 필요가 없으므로 break
        if cnt1 < 0 or cnt2 < 0 or cnt3 < 0 or cnt4 < 0:
            break
    
    # 모든 변수가 0이어야 완전 괄호 성립
    if cnt1 == 0 and cnt2 == 0 and cnt3 == 0 and cnt4 == 0:
        result.append("1")
    else:
        result.append("0")
        
# 결과 출력
for h in range(1, 11):
    print(f"#{h}", result[h-1])