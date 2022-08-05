import sys

sys.stdin = open("_조교의성적매기기.txt")
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    maxtrix = [list(map(int, input().split())) for _ in range(n)]
    credit = { 0.1 :'A+', 0.2 :'A0', 0.3 :'A-', 0.4 :'B+', 0.5 :'B0', 0.6 :'B-', 0.7 :'C+', 0.8 :'C0', 0.9 :'C-', 1 :'D0'}

    board = []
    for j in maxtrix:
        total = j[0] * 0.35 + j[1] * 0.45 + j[2] * 0.2 # 전제 성적을 board 리스트에 추가
        board.append(total)
    
    rank = []
    rev = sorted(board, reverse= True) # 순위를 구하기 위해서 board를 역으로 정렬한 후, 인덱스 값을 rank 리스트에 추가해줌
    for j in board:
        rank.append(rev.index(j) + 1)   
    
    print(f'#{i + 1}', end=' ')
    for key, val in credit.items(): # 인덱스 값이므로, k에 -1 을 해줌 
        if rank[k - 1] / n <= key:
            print(val)
            break