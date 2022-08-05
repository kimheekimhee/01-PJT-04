import sys

t = 10
for i in range(1, t + 1):
    n = int(input())
    b = input()
    stack = []

    for item in b:
        if stack:
            if item == '{':
                stack.append(item)
            elif item == '[':
                stack.append(item)
            elif item == '(':
                stack.append(item)
            elif item == '<':
                stack.append(item)

            elif item == '}':
                if stack == '{':
                    stack.pop()
                else:
                    stack.append(item)
            elif item == ']':
                if stack == '[':
                    stack.pop()
                else:
                    stack.append(item)
            elif item == ')':
                if stack == '(':
                    stack.pop()
                else:
                    stack.append(item)
            elif item == '>':
                if stack == '<':
                    stack.pop()
                else:
                    stack.append(item)


        else:
            stack.append(item)
        
    if stack:
        print(f'#{i}', '1')
    
    else:
        print(f'#{i}', '0')
        
sys.stdin = open("_괄호짝짓기.txt")
