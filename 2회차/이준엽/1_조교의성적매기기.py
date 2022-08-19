t = int(input())
for _ in range(1,t+1):
    n,k = map(int,input().split())
    scores = []
    for i in range(1,n+1):
        mid,fin,sub = map(int,input().split())
        score = (mid*0.35)+(fin*0.45)+(sub*0.2)
        scores.append(score)
    k_scores = scores[k-1]
    sort_scores = sorted(scores, reverse=True)
    k_scores_rank = sort_scores.index(k_scores)
    if k_scores_rank <= n/10-1:
        rank = 'A+'
    elif k_scores_rank <= ((n/10)*2)-1:
        rank = 'A0'
    elif k_scores_rank <= ((n/10)*3)-1:
        rank = 'A-'
    elif k_scores_rank <= ((n/10)*4)-1:
        rank = 'B+'
    elif k_scores_rank <= ((n/10)*5)-1:
        rank = 'B0'
    elif k_scores_rank <= ((n/10)*6)-1:
        rank = 'B-'
    elif k_scores_rank <= ((n/10)*7)-1:
        rank = 'C+'
    elif k_scores_rank <= ((n/10)*8)-1:
        rank = 'C0'
    elif k_scores_rank <= ((n/10)*9)-1:
        rank = 'C-'
    elif k_scores_rank <= ((n/10)*10)-1:
        rank = 'D0'
    print(f'#{_}',rank)
    