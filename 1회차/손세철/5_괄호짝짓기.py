import sys

sys.stdin = open("_괄호짝짓기.txt")

for tc in range(10):
    N = int(input())
    list_ = list(map(str, input()))
    stack = list()

left = ['{','[','(','<']
right = ['}',']',')','>']

for i in range(N):
    if list_[i] in left:
        stack.append(list_[i])
    if list_[i] in right:
        if right == left:
            stack.pop()
        else:
            break
result = 0
if len(stack) == 0:
    result = 1
print("#{} {}".format(tc + 1, result))