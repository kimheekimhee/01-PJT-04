import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())
Rank_list = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for i in range(T):
    N, K = map(int, input().split())
    
    N_point = []
    N_point_target = 0
    for j in range(N):
        x, y, z = map(int, input().split())
        N_point.append(x*0.35+y*0.45+z*0.2)
        if j+1 == K:
            N_point_target = x*0.35+y*0.45+z*0.2
        
    N_point.sort(reverse=True)

    N_point_rank = int((N_point.index(N_point_target))/(N/10))
    
    print(f'#{i+1}', Rank_list[N_point_rank])
    
    
        