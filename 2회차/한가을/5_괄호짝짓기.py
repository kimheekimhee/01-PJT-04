import sys

sys.stdin = open("_괄호짝짓기.txt")

# 4 종류의 괄호문자들 '()', '[]', '{}', '<>'로 이루어진 문자열이 주어진다
# 문자열에 사용된 괄호들의 짝이 모두 맞는지 판별하라

# 총 10개의 테스트 케이스가 주어진다
# 각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 길이가 주어지면
# 다음 줄에 테스트 케이스가 주어진다

# 유효하면(짝이 맞으면) 1, 그렇지 않으면 0 출력

for tc in range(1, 11):
    tcLength = int(input())
    bracket = list(map(str, input()))
    stack = []

    left = ['(', '[', '{', '<']
    right = [')', ']', '}', '>']

    for i in range(tcLength):
        if bracket[i] in left:
            stack.append(bracket[i])
        elif bracket[i] in right:
            #* 가장 상위의 괄호 값과 쌍이라면
            if right.index(bracket[i]) == left.index(stack[-1]):
                #* 상위의 원소 제거
                stack.pop()
            else:
                break
    
    result = 0

    if len(stack) == 0:
        result = 1

    print(f'#{tc} {result}')