import sys

sys.stdin = open("_조교의성적매기기.txt")

def rank_(num,rank): #인원수를 10등분 
    if rank <= num*(0.1):
        result = 'A+'
    elif rank <= num*(0.2):
        result = 'A0'
    elif rank <= num*(0.3):
        result = 'A-'
    elif rank <= num*(0.4):
        result = 'B+'
    elif rank <= num*(0.5):
        result = 'B0'
    elif rank <= num*(0.6):
        result = 'B-'
    elif rank <= num*(0.7):
        result = 'C+'
    elif rank <= num*(0.8):
        result = 'C0'
    elif rank <= num*(0.9):
        result = 'C-'
    elif rank <= num*(1):
        result = 'D0'

    return result

T = int(input())

for _ in range(T):
    M, K = map(int,input().split())
    M_list = [list(map(int,input().split()))for a in range(M)]
    K_list = M_list[K-1]
    K_score = 0.35*K_list[0] + 0.45*K_list[1] + 0.2*K_list[2]

    M_score = [] #점수맥이기

    for a in range(M):
        score = 0.35*M_list[a][0] + 0.45*M_list[a][1] + 0.2*M_list[a][2]
        M_score.append(score)
    M_score.sort(reverse= True)
    #print(M_score, K_score)
    K_rank = 0
    for b in range(M):
        if M_score[b] == K_score:
            K_rank = b+1
    
    print(f'#{_+1}', rank_(M,K_rank))