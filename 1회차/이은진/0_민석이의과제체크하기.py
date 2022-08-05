import sys
sys.stdin = open("_민석이의과제체크하기.txt")

for t in range(1, int(input())+1):
    x, y = map(int, input().split())
    do_hw = list(map(int, input().split()))
    no_hw = []
    for i in range(1, x+1):
        if i not in do_hw:
            no_hw.append(str(i))
    a = ' '.join(no_hw)
    print(f'#{t} {a}')