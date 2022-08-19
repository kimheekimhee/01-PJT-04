import sys

sys.stdin = open("_조교의성적매기기.txt")

n = int(input())

for num in range(1, n+1) :
    stu, k = map(int, input().split())
    
    stu_score = []
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 
    'C+', 'C0', 'C-', 'D0']
    stu_range = stu / 10

    for s in range(1, stu+1) :
        mid, fin, rep = map(int, input().split())
        mid = mid * 0.35
        fin = fin * 0.45
        rep = rep * 0.2
        
        stu_score.append(round(mid+fin+rep, 2))
    
    stu_score_sort = sorted(stu_score, reverse=True)

    stu_score_grade = []
    for sss in range(len(stu_score_sort)) :
        if sss < stu_range :
            stu_score_grade.append(grade[0])

        elif sss < (stu_range * 2) and sss >= stu_range :
            stu_score_grade.append(grade[1])

        elif sss < (stu_range * 3) and sss >= (stu_range * 2) :
            stu_score_grade.append(grade[2])

        elif sss < (stu_range * 4) and sss >= (stu_range * 3) :
            stu_score_grade.append(grade[3])

        elif sss < (stu_range * 5) and sss >= (stu_range * 4) :
            stu_score_grade.append(grade[4])

        elif sss < (stu_range * 6) and sss >= (stu_range * 5) :
            stu_score_grade.append(grade[5])

        elif sss < (stu_range * 7) and sss >= (stu_range * 6) :
            stu_score_grade.append(grade[6])

        elif sss < (stu_range * 8) and sss >= (stu_range * 7) :
            stu_score_grade.append(grade[7])

        elif sss < (stu_range * 9) and sss >= (stu_range * 8) :
            stu_score_grade.append(grade[8])
        
        else :
            stu_score_grade.append(grade[9])

    k_score = stu_score_sort.index(stu_score[k-1])
    k_grade = stu_score_grade[k_score]

    print(f'#{num} {k_grade}')