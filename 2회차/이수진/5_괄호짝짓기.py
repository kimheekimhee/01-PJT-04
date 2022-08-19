import sys

sys.stdin = open("_괄호짝짓기.txt")

for t in range(10):
    n=int(input())
    string=input()
    stack = []
    flag = True
    for i in range(n):
        if string[i] in '{[(<':
            stack.append(string[i])
        elif string[i] in '}])>':
            if stack:
                pop = stack.pop()
                if (pop == '(' and string[i] == ')') or (pop == '[' and string[i] == ']') or (pop == '{' and string[i] == '}') or (pop == '<' and string[i] == '>'):
                    flag = True
                else:
                    flag = False
                    break
            else:
                flag = False
                break
    print(f'#{t+1} {1 if flag else 0}')

    # 스택 활용
    # 열린괄호가 나오면 스택에 push한다
    # 닫힌괄호가 나오면 스택의 열린괄호를 pop하고, 두 열림-닫힘 괄호가 같은 종류인지 검사
    # 서로 다른 종류일 경우 0이 출력된다.