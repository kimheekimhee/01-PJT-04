import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())

    scholar = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    score = []
    for a in scholar:
        for b in range(N//10):
           score.append(a)

    total = []
    for a in range(N):
        a,b,c =map(int, input().split())
        total.append(0.35*a + 0.45*b + 0.2*c)
    new_total = sorted(total)
    new_total.reverse()

    result ={}
    for a in range(N):
           result[new_total[a]] = result.get(new_total[a],'') + score[a] 
    
    print(f'#{test_case} {result.get(total[K-1])}')
    
    
    
    



