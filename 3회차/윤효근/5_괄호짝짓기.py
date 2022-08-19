import sys

sys.stdin = open("_괄호짝짓기.txt")
for test_case in range(10):
    n=int(input())
    s=list(map(str,input()))
    stack = []
    result = 0
    open_list=['(','{','[','<']
    close=[')','}',']','>']
    for i in range(n):
        if s[i] in open_list:
            stack.append(s[i])
        if s[i] in close:
            if close.index(s[i]) == open_list.index(stack[-1]):
                stack.pop()
            else:
                break
    if len(stack) == 0:
        result = 1
    print(f'#{test_case+1} {result}')
