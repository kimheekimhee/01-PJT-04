import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

for tc in range(1, T + 1):
    # n 수강생 수, s 제출한 사람 수
    n, s = map(int, input().split())
    
    # input에 들어오는 번호는 제출한 사람들 번호
    submit = list(map(int, input().split()))
    
    no_submit = []
    
    for i in range(1, n + 1):
        if i not in submit:
            no_submit.append(i)
            
    print(f'#{tc}', *no_submit)