import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())
for z in range(T):
    N,K = map(int, input().split())
    scorelst = []
    for y in range(N):
        score = list(map(int, input().split()))
        personscore=score[0]*0.35+score[1]*0.45+score[2]*0.2
        scorelst.append(personscore)
    target = scorelst[K-1]
    scrlst = sorted(scorelst, reverse=True)
    for i in range(N):
        if target == scrlst[i]:
            rank = i
    hakjum = rank//(N//10)
    scrset = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    print(f'#{z+1} {scrset[hakjum]}')