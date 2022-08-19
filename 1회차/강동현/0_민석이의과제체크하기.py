import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())
for z in range(T):
    st, hw = map(int, input().split())
    lst = list(map(int, input().split()))
    std = []
    for i in range(1,st+1):
        if i not in lst:
            std.append(str(i))
    answer = ' '.join(std)
    print(f'#{z+1} {answer}')