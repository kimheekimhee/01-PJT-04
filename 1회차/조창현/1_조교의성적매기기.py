from pprint import pprint
import sys

sys.stdin = open("_조교의성적매기기.txt")

t = int(input())
for t in range(1, t + 1):
    n, k = map(int, input().split())
    rank_num = {}
    
    for i in range(n):
        mt, ft, rep = map(int, input().split())
        #print(mt, ft, rep)
        total = (mt * 0.35) + (ft * 0.45) + (rep * 0.2)
        #print(total)
        rank_num[i+1] = total
    #pprint(rank_num)

    rank_cnt = 0
    for i in range(n):
        if rank_num[k] <= rank_num[i + 1]:
            rank_cnt += 1
    #print(rank_cnt)

    if rank_cnt <= (1 / 10) * n:
        print(f'#{t} A+')
    elif rank_cnt <= (2 / 10) * n:
        print(f'#{t} A0')
    elif rank_cnt <= (3 / 10) * n:
        print(f'#{t} A-')
    elif rank_cnt <= (4 / 10) * n:
        print(f'#{t} B+')
    elif rank_cnt <= (5 / 10) * n:
        print(f'#{t} B0')
    elif rank_cnt <= (6 / 10) * n:
        print(f'#{t} B-')
    elif rank_cnt <= (7 / 10) * n:
        print(f'#{t} C+')
    elif rank_cnt <= (8 / 10) * n:
        print(f'#{t} C0')
    elif rank_cnt <= (9 / 10) * n:
        print(f'#{t} C-')
    elif rank_cnt <= (10 / 10) * n:
        print(f'#{t} D0')