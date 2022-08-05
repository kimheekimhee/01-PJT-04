import sys

sys.stdin = open("_괄호짝짓기.txt")

for test_case in range(1, 10+1):
    N = int(input())
    char = input()

    stack = []
    valid = True

    for i in char:
        if i =='(' or i == '[' or i == '{' or i == '<':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                valid = False
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                valid = False
                break
        elif i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                valid = False
                break
        elif i == '>':
            if stack and stack[-1] == '<':
                stack.pop()
            else:
                valid = False
                break               
        
    if not stack:
        if valid:
            print(f'#{test_case} 1')
        else:
            print(f'#{test_case} 0')
    else:
        print(f'#{test_case} 0')