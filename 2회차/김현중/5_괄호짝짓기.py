import sys

sys.stdin = open("_괄호짝짓기.txt")
input = sys.stdin.readline
open_ = '([{<'
close_ = ')]}>'

for test_case in range(1, 11):
    check = True
    T = int(input())
    lines = input().strip()
    line_lst = []
    for i in lines:
        if i in open_:
            line_lst.append(i)
        elif i in close_:
            if close_.index(i) == open_.index(line_lst.pop()):
                continue
            else:
                check = False
                break
        
    if check == False:
        print(f'#{test_case} 0')
    else: print(f'#{test_case} 1')