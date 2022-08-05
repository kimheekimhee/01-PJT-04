import sys

sys.stdin = open("_괄호짝짓기.txt")

for test in range(1, 11):
    num = int(input())
    sen = list(input())

    check = []
    for i in sen:
        if i =='(' or i == '[' or i == '{' or i =='<':
            check.append(i)
            # 열리는 괄호의 경우 아직 나온 상황에서 짝을 확인 안 해도 되니 리스트에 추가하여 줍니다.
        elif i ==')':
            if check[-1] != '(':
                print(f'#{test} 0')
                break
            else:
                check.pop()
        elif i == ']':
            if check[-1] != '[':
                print(f'#{test} 0')
                break
            else:
                check.pop()
        elif i == '}':
            if check[-1] != '{':
                print(f'#{test} 0')
                break
            else:
                check.pop()
        elif i == '>':
            if check[-1] != '<':
                print(f'#{test} 0')
                break
            else:
                check.pop()
        # 닫힌 괄호의 경우 리스트의 마지막에 저장된 괄호가 본인의 짝인지 확인하고 맞으면 팝하고 아니면 
        # 식이 성립할 수 없으니 식이 성립할 수 없다고 해주고 브레이크를 걸어줍니다.
    else:
        if len(check) !=0:
            print(f'#{test} 0')
    # 문자열를 다 돌았는데 리스트에 저장된 값이 있으면 닫히지 않은 괄호가 있으니 식이 성립할 수 없습니다.
        else:    
            print(f'#{test} 1')
    # 이외의 경우는 식이 성립한기에 1을 출력해줍니다.
