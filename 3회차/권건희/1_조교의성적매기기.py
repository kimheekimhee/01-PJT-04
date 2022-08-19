import sys

sys.stdin = open("_조교의성적매기기.txt")
T=int(input())
for _ in range(T):
    N,K=map(int,input().split())
    score_={}
    list_=[]
    for a in range(1,N+1):
        m,f,w=map(int,input().split())
        all=m*25/100+f*45/100+w*20/100
        score_[a]=all
        list_.append(all)
    list_.sort(reverse=1) 
    for n in range(N):
        for i in range(1,N+1):
            if list_[n]==score_[i]:
                if n<= 9:
                    score_[i]='A+'
                else: 
                    if n<= 19:
                        score_[i]='A0'
                    else:
                        if n<=29:
                            score_[i]='A-'
                        else:
                            if n<=39:
                                score_[i]='B+'

                            else:
                                if n<=49:
                                    score_[i]='B0'
                                else:
                                    if n<=59:
                                        score_[i]='C+'
                                    else:
                                        if n<=69:
                                            score_[i]='C0'
                                        else:
                                            if n<=79:
                                                score_[i]='C-'
                                            else:
                                                score_[i]='D0' 
    print(f'#{_+1}',score_[K])       