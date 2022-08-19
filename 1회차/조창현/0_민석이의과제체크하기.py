import sys

sys.stdin = open("_민석이의과제체크하기.txt")

t = int(input())

for t in range(1, t + 1):
    n, k = map(int, input().split())
    done_list = list(map(int, input().split()))
    #print(done_list)
    none_list = []
    for i in range(1, n + 1):
        if i not in done_list:
            none_list.append(i)
    print(f'#{t} ',end = '')    
    for i in range(n - k):
        print(none_list[i], end = ' ')
    print('')
