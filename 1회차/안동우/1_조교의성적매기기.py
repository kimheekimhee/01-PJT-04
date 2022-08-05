import sys

sys.stdin = open("_조교의성적매기기.txt")

T=int(input())
s=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
for q in range(1,T+1):
    N,K=map(int,input().split())# N학생수 K학점을 알고싶은 학생의 번호
    e=[]
    for i in range(N):
        a,b,c=map(int,input().split())
        w=(a*0.35)+(b*0.45)+(c*0.2)
        e.append(w)


    r=e[K-1]
    e.sort(reverse=True)
    
    y=N//10
    u=e.index(r)//y
    print("#%d %s"% (q,s[u]))