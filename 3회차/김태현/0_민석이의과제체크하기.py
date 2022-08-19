import sys
sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

for i in range(1, T+1):
    done, not_done = map(int, input().split())
    done_idx = list(map(int, input().split()))

    result = []
    for j in range(1, done+1):
        if j not in done_idx:
            result.append(j)
    
    print(f"#{i}", *result)

