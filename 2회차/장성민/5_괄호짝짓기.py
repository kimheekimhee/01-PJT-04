import sys

sys.stdin = open("_괄호짝짓기.txt")

for tc in range(1, 11):
    n = int(input())
    string = input()

    left = []
    result = 1
    for i in range(n):
        if string[i] == '(' or string[i] == '{' or string[i] == '[' or string[i] == '<':
            left.append(string[i])

        if string[i] == ')':
            if len(left) > 0 and left.pop() != '(':
                result = 0
                break
        if string[i] == '}':
            if len(left) > 0 and left.pop() != '{':
                result = 0
                break
        if string[i] == ']':
            if len(left) > 0 and left.pop() != '[':
                result = 0
                break
        if string[i] == '>':
            if len(left) > 0 and left.pop() != '<':
                result = 0
                break

    print(f'#{tc} {result}')