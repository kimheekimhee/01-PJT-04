import sys

sys.stdin = open("_괄호짝짓기.txt")

T = 10 # 테스트케이스 개수

for test_case in range(T):
    case_length = int(input()) # 케이스마다 길이 저장할 변수
    case_list = list(map(str, input())) # 케이스마다 괄호 리스트 저장
    result = 0 # 마지막에 유효한지 1 or 0 출력할 변수
    flag = -1 # 짝이 맞는 괄호가 없고, 리스트를 끝까지 돌았을때 사용할 flag 변수
    
    while flag != 1: # flag 변수가 변화하기 전까지 while문으로 반복
        for i in range(len(case_list)): 
            if case_list[i] == '(' and case_list[i+1] == ')': # 소괄호 짝 체크
                case_list.pop(i) # 발견하면 pop 두 번으로 짝을 꺼낸다.
                case_list.pop(i)
                break # 그리고 break 문으로 for문 벗어난 뒤, while문 다시 시작
            if case_list[i] == '{' and case_list[i+1] == '}': # 중괄호 짝 체크
                case_list.pop(i)
                case_list.pop(i)
                break
            if case_list[i] == '[' and case_list[i+1] == ']': # 대괄호 짝 체크
                case_list.pop(i)
                case_list.pop(i)
                break
            if case_list[i] == '<' and case_list[i+1] == '>': # '<','>'괄호 짝 체크
                case_list.pop(i)
                case_list.pop(i)
                break
        else:
            flag = 1 # 남은 list의 길이를 다 돌았는데 발견못했을때 종료를 위한 flag변수 를 1로.
            break

    if flag == 1 and len(case_list) > 0: # flag변수가 1이고, 길이가 남았을때 유효여부 0
        result = 0
    else:
        result = 1
    print(f'#{test_case + 1} {result}')