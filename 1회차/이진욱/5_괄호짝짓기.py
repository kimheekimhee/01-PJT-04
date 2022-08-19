import sys

sys.stdin = open("_괄호짝짓기.txt")

for t in range(10):
    n = int(input())
    S = input()
    ans = ''
    for i in S:
        if i in ['(',')','[',']','{','}','<','>'   ]:
            ans += i


    while True:

        ans_new = ans.replace('()','')
        ans = ans_new
        ans_new = ans.replace('[]', '')
        ans = ans_new
        ans_new = ans.replace('{}', '')
        ans = ans_new
        ans_new = ans.replace('<>', '')
        ans = ans_new


        if '()' not in ans and '[]' not in ans and '{}' not in ans and '<>' not in ans:
            break


    if len(ans) == 0:
        print(f'#{t+1} {1}')
    else:
        print(f'#{t+1} {0}')