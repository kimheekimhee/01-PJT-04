import sys
sys.stdin = open("_괄호짝짓기.txt")

T = 10
for i in range(T):
    N = int(input())
    word = input()

    stack1 = []
    result = 1
   
    for j in range(N):
        if word[j] == '(' or word[j] == '{' or word[j] == '[' or word[j] == '<':
            stack1.append(word[j])

        if word[j] == ')':
            if len(stack1) > 0 and stack1.pop() != '(':
                result = 0
                break
        if word[j] == '}':
            if len(stack1) > 0 and stack1.pop() != '{':
                result = 0
                break
        if word[j] == ']':
            if len(stack1) > 0 and stack1.pop() != '[':
                result = 0
                break
        if word[j] == '>':
            if len(stack1) > 0 and stack1.pop() != '<':
                result = 0
                break



    print(f'#{i+1} {result}')
