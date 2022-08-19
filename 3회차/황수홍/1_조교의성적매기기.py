import sys

sys.stdin = open("_조교의성적매기기.txt")

input = sys.stdin.readline

T = int(input())
grade = ['D0','C-','C0','C+','B-','B0','B+','A-','A0','A+']
for i in range(T):
    N, K = map(int,input().split())
    sum = []
    for j in range(N):
        a, b, c = map(int,input().split())
        sum.append((a*0.35)+(b*0.45)+(c*0.2))
    s = sorted(sum)
    for k in range(len(s)):
        if sum[K-1] == s[k]:
            print(f'#{i+1} {grade[int(k/N*10)]}')
