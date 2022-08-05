import sys

sys.stdin = open("_괄호짝짓기.txt")

from pprint import pprint
T = 10

for t in range(1, T+1):
    b_len = int(input())
    brackets = list(input())

    dict_ = {
        '(' : ')',
        '{' : '}', 
        '[' : ']', 
        '<' : '>'}
    
    queue = []
    for idx in range(b_len):
        for key, value in dict_.items(): 
            if brackets[idx] == key:
                queue.append(dict_[key])
            elif brackets[idx] == value:
                if value in brackets[idx]:
                    queue.pop()
            # if len(deque) == 0:
            #     continue
                # print(result_stack)
    # print(result_stack)
    result = 1
    if len(queue) != 0:
        result = 0
    # result = 1
    # if len(result_stack) != 0:
    #     result = 0

    print(f'#{t} {result}')