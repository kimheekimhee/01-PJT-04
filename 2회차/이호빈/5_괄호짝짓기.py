import sys

sys.stdin = open("_괄호짝짓기.txt")
T = 10

for tc in range(1, T+1):
    N = int(input())
    pair = list(map(str, input()))
    stack = []

    #왼쪽 괄호
    left = ["(", "{", "[", "<"]
    #오른쪽 괄호
    right = [")", "}", "]", ">"]

    for i in pair:
        #i가 left에 있으면 stack에 추가해주고
        if i in left:
            stack.append(i)
        #i가 right에 있으면 left가 추가된 stack의 가장 마지막 요소랑 같으면 pop을 해준다
        if i in right:
            if right.index(i) == left.index(stack[-1]):
                stack.pop()
            else:
                break
    #만약 길이가 0이면 짝이 맞는 거니까 1을 출력해주고 아니면 0을 출력해준다.
    if len(stack) == 0:
        result = 1
    else:
        result = 0
    
    print(f"#{tc} {result}")