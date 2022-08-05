# 학생 수 N, 학점 알고싶은 학생 번호 K,
# 학생이 받은 시험 및 과제 점수 3개, 
# 총점 = 중간(35%)+기말(45%)+과제(20%)
# 평점 A+,A0,A-,B+,B0,B-,C+,C0,C-,D0
# num, id = 10,2
# scores = [[87, 59, 88], 
#             [99, 94, 78], 
#             [94, 86, 86], 
#             [99, 100, 99],
#             [69, 76, 70], 
#             [76, 89, 96], 
#             [98, 95, 96], 
#             [74, 69, 60], 
#             [98, 84, 67], 
#             [85, 84, 91]]
import sys
sys.stdin = open("_조교의성적매기기.txt")
T = int(input())
for test_case in range(1,T+1):
    num, where = map(int,input().split())
    scores = []
    for _ in range(num):
        temp = list(map(int,input().split()))
        scores.append(temp)
    std_total = []
    for score in scores:
        mt = score[0]*35/100
        ft = score[1]*45/100
        sub = score[2]*20/100
        total = mt+ft+sub
        std_total.append(total)
    sort_std_total = sorted(std_total)
    # print(std_total[id-1])
    rank = sort_std_total.index(std_total[where-1])   # 정렬된 총점
    grade = int(rank/num * 10)
    grade_lst = ['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']
    std_grd = grade_lst[grade]
    result = std_grd
    print(f'#{test_case} ',result)