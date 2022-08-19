import sys

sys.stdin = open("_괄호짝짓기.txt")
T = 10
dic = {')':'(',
        ']':'[',
        '}':'{',
        '>':'<'}
for test_case in range(1,T+1):

    str_len = int(input())
    s = input()
    stack = []
    result = 1

    for s in s:
        if s in '([{<':
            stack.append(s)
        else :
            if stack[-1] == dic[s]:
                stack.pop()
            else : result = 0
    if len(stack) != 0:
        result = 0
    print(f'#{test_case}',result)