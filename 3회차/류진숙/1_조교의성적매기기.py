import sys

sys.stdin = open("_조교의성적매기기.txt")

from pprint import pprint

T = int(input())


for t in range(1, T+1):
    
    n, k = list(map(int, input().split()))
    gp = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-']

    
    score_list = []
    for i in range(n):
        mid, final, hw = list(map(int, input().split()))
        sum_score = (mid * 0.35) + (final * 0.45) + (hw * 0.2)
        score_list.append([sum_score, i+1])

    score_li = sorted(score_list, reverse=True)

    n_gp = n // 10

    cnt = 0
    
        

    # cnt = 0
    # for key, value in gp.items():
    #         if cnt != n_gp:
    #             gp[key].append(score_li[n_gp])
    #             cnt += 1
    #         else:
    #             cnt = 0
    #             break

    # print(gp)       
        

    
        