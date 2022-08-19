# import sys

# sys.stdin = open("_괄호짝짓기.txt")

# 딕셔너리를 활용하여 여는 괄호인 경우 해당 키 값의 밸류 +1, 닫는 경우 해당 키 값의 밸류 -1를 하고 
# 마지막에 모든 value가 0인 경우 1, 아니면 0을 출력하는 방법을 생각해냈습니다.
# 위의 방법이 더 간단할 것 같았지만
# 이번주에 배운 스택을 활용하려다 보니 조건이 너무 많아진 것 같습니다.
# 그런데 스택을 활용하기 위한 다른 방법들은 생각나지 않아 다른 분들의 코드를 확인해봐야 할 것 같습니다.

# 10개의 테스트 케이스
for test_case in range(1, 11):
    # 값 입력
    N = int(input())
    list_ = list(map(str, input()))

    # 유효성 여부를 위한 변수
    is_paried = 1

    # 4종류의 괄호 문자들을 담기 위한 list 생성
    gh_1 = []
    gh_2 = []
    gh_3 = []
    gh_4 = []

    # 여는 괄호일 경우 해당 list에 append
    # 닫는 괄호일 경우 해당 list에서 빼낼 수 있으면 pop, 빼낼 수 없으면 유효성 여부를 0으로 만든 뒤 break
    for gh in list_:
        if gh == '(':
            gh_1.append(gh)
        elif gh == ')':
            if len(gh_1) != 0:
                gh_1.pop()
            else:
                is_paried = 0
                break
        elif gh == '[':
            gh_2.append(gh)
        elif gh == ']':
            if len(gh_2) != 0:
                gh_2.pop()
            else:
                is_paried = 0
                break
        elif gh == '{':
            gh_3.append(gh)
        elif gh == '}':
            if len(gh_3) != 0:
                gh_3.pop()
            else:
                is_paried = 0
                break
        elif gh == '<':
            gh_4.append(gh)
        elif gh == '>':
            if len(gh_4) != 0:
                gh_4.pop()
            else:
                is_paried = 0
                break

    print(f'#{test_case}', end=' ')
    # 유효성 변수가 1이고(닫는 기호가 더 많지 않을 때)
    # 각각의 list들이 비어있다면(여는 기호가 더 많지 않을 때) 1 출력
    # 둘 중 하나라도 만족하지 않는다면 0 출력
    if is_paried == 1 and gh_1 == [] and gh_2 ==[] and gh_3 ==[] and gh_4 == []:
        print(1)
    else:
        print(0)