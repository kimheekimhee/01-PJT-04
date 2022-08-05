import sys

sys.stdin = open("_괄호짝짓기.txt")

# 테스트의 길이 주어짐
T = map(int, input().split())
stack = []

for _ in range(n, n+1):
    T = int(input())
    if T != 0: # T가 0이 아니면
        stack.pop() # stack에서 뺌
        if T == 1:
            stack.append()

print(stack) # stack 출력
print(T) # T 출력