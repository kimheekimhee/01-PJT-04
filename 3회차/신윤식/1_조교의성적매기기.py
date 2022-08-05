# import sys

# sys.stdin = open("./3회차/신윤식/_조교의성적매기기.txt")



T = int(input())

for _ in range(1, T+1):

    N, K = map(int,input().split())
    a = N//10
    score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    dict_score = {}
    for i in score:
        dict_score[i] = a
    print(dict_score)



#     for i in range(N):
#         score.insert(a*i, score[a*i])
#     print(score)
# #     total = 0    
#     total_lst = []

#     for i in range(N):
#         mid, end, home = map(int,input().split())
#         total = mid * 0.35 + end * 0.45 + home * 0.2
#         total_lst.append(total)
    
#     total_lst.sort(reverse=True)
#     print(total_lst)


# # 30 12
# 76 88 86
# 100 89 91
# 91 90 83
# 86 82 96
# 78 76 98
# 94 85 96
# 80 91 97
# 63 63 58
# 97 100 99
# 95 76 89
# 97 88 96
# 76 76 96
# 89 82 99
# 62 95 83
# 63 88 60
# 74 77 72
# 98 87 92
# 99 84 58
# 74 76 99
# 81 81 84
# 79 100 72
# 97 88 98
# 97 94 98
# 96 66 74
# 87 89 87
# 69 73 95
# 89 97 91
# 82 94 85
# 85 89 75
# 89 80 91