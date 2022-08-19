# import sys

# sys.stdin = open("_괄호짝짓기.txt")
for _ in range(1, 11):
    N = int(input())
    S = input()
    stack = []
    result = -1

    for i in S:
        # i가 ( 거나 [ 거나 { 거나 < 라면
        if i == "(" or i == "[" or i == "{" or i == "<": 
            stack.append(i) # 스택에 i값 추가
        # 각 괄호 별 반대쪽 괄호가 있다면     
        elif i == "]":
            if len(stack) != 0 and stack[-1] == "[": # 스택의 길이가 0이 아니거나 스택의 마지막값이 시작괄호면
                stack.pop() # 해당 괄호를 스택에서 빼낸다.
            else:
                stack.append("]") # 그외에 스택에서 끝 괄호를 추가
                break
        elif i == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(")")
                break
        elif i == "}":
            if len(stack) != 0 and stack[-1] == "{":
                stack.pop()
            else:
                stack.append("}")
                break
        elif i == ">":
            if len(stack) != 0 and stack[-1] == "<":
                stack.pop()
            else:
                stack.append(">")
                break

    if len(stack) == 0: # 스택의 길이가 0이면 다 빠져나갔으므로 
        result = 1 # 결과는 1
    else:
        result = 0 # 그외엔 0
    print("#{} {}".format(_, result))