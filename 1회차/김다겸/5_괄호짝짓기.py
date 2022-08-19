# import sys

# sys.stdin = open("_괄호짝짓기.txt")

for t in range(1, 11):
    n = int(input())
    # 괄호들 입력받기
    list_ = list(input())

    # stack 리스트 생성
    stack = []

    left = ['(', '[', '{', '<']
    right = [')', ']', '}', '>']

    for i in range(n):
        # 입력받은 list_의 원소가 left의 괄호이면
        if list_[i] in left:
            # stack에 추가
            stack.append(list_[i])
        # 입력받은 list_의 원소가 right의 괄호이면
        if list_[i] in right:
            # right의 list_[i] 번째 인덱스와 left의 stack[-1] 번째 인덱스 같으면
            if right.index(list_[i]) == left.index(stack[-1]):
                # stack의 마지막 원소 pop
                stack.pop()
            else:
                break
    
    print(f'#{t}', end=' ')
    if len(stack) == 0:
        print(1)
    else:
        print(0)