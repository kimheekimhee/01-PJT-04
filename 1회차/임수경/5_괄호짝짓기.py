import sys

sys.stdin = open("_괄호짝짓기.txt")


T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = input()

    stack1 = []
    result = 1
    
    for i in range(N):
        if arr[i] == '(' or arr[i] == '{' or arr[i] == '[' or arr[i] == '<':
            stack1.append(arr[i])

        if arr[i] == ')':
            if len(stack1) > 0 and stack1.pop() != '(':
                result = 0
                break
        if arr[i] == '}':
            if len(stack1) > 0 and stack1.pop() != '{':
                result = 0
                break
        if arr[i] == ']':
            if len(stack1) > 0 and stack1.pop() != '[':
                result = 0
                break
        if arr[i] == '>':
            if len(stack1) > 0 and stack1.pop() != '<':
                result = 0
                break



    print("#{} {}".format(tc,result ))