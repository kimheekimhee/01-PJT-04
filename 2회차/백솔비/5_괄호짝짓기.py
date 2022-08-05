import sys
sys.stdin = open("_괄호짝짓기.txt")

T = 10

for tc in range(1, T+1):
    N = int(input())
    list_ = list(input())
    
    #넣고 뒤에서 빼는 방식이므로 stack을 설정합니다.
    stack = []
    flag = 1

    #먼저 stack에 여는 괄호를 다 집어 넣어줍니다.
    for i in range(N):
        if list_[i] == '(' or list_[i] == '[' or list_[i] == '{' or list_[i] == '<':
            stack.append(list_[i])
        
        # 닫는 괄호가 올 때, 전체 스택의 길이가 0이 아니고 (0이어야 다 맞아 떨어지는 괄호들로만 구성) 
        # 뒤에서 뺀 괄호가 닫는 괄호가 짝이 아닐 경우 실패이므로 flag를 0으로 잡아주고 break를 걸어줍니다.
        elif list_[i] == ')':
            if len(stack) != 0 and stack.pop() != '(':
                flag = 0
                break
        elif list_[i] == ']':
            if len(stack) != 0 and stack.pop() != '[':
                flag = 0
                break
        elif list_[i] == '}':
            if len(stack) != 0 and stack.pop() != '{':
                flag = 0
                break
        elif list_[i] == '>':
            if len(stack) != 0 and stack.pop() != '<':
                flag = 0
                break
     
                
    print(f'#{tc} {flag}')