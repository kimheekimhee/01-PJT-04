import sys

sys.stdin = open("_괄호짝짓기.txt")

for test_case in range(1, 11):
    n = int(input())
    bracket = input()
    stack = []
    # 여는 괄호들
    left = ["<", "{", "[", "("]
    # 닫는 괄호들
    right = [">", "}", "]", ")"]

    # 올바른 것
    answer = 1
    for i in bracket:
        if i in left:
            stack.append(i)
        else:
            # 닫는 괄호중 서로의 인덱스가 동일하면 팝
            if left.index(stack[-1]) == right.index(i):
                stack.pop()
            # 그게 아니라면 올바르지않는 괄호이므로 answer = 0
            else:
                answer = 0
                break
    print(f"#{test_case} {answer}")