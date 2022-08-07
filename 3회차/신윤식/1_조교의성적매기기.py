import sys

sys.stdin = open("./3회차/신윤식/_조교의성적매기기.txt")

T = int(input())

for _ in range(1, T+1):

    N, K = map(int,input().split())
    a = N//10
    score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0'] * a
    dict_avg = {}
    for i in range(N):
        mid, end, home = map(int,input().split())
        total = mid * 0.35 + end * 0.45 + home * 0.2
        dict_avg[i] = total

    sort = sorted(dict_avg.items(), key=lambda x:-x[1])
    sort = list(map(list,sort))
    o = 0
    for j in range(0,len(sort),a):
        for k in range(a):
            sort[j+k].append(score[o])
        o += 1
    print(f'#{_} {sorted(sort, key=lambda x:x[0])[K-1][2]}')