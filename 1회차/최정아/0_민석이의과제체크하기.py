import sys

sys.stdin = open("_민석이의과제체크하기.txt")

stack = []

for _ in range(n, n+1):
    # 테스트 케이스의 수 T 주어짐
    T = int(input())
    # T가 0보다 클 때 
    if T > 0:
        # stack에서 뺌
        stack.pop()
    else: # 아니면
        stack.append() # stack에 추가
        stack.sort() # sort 통해서 stack 정렬

print(stack)