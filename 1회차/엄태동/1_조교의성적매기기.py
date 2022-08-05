import sys

sys.stdin = open("_조교의성적매기기.txt")
T=int(input())
for i in range(T):
    Student, Student_num = map(int, input().split())
    Score=[list(map(int, input().split())) for j in range(Student)]
    for k in range(Student):
        Score[k]=Score[k][0]*0.35 + Score[k][1]*0.45 + Score[k][2]*0.2
    New_Score=list(reversed(sorted(Score)))
    for k in range(Student):
        for j in range(Student):
            if New_Score[k] == Score[j]:
                Score[j]=k+1
    for m in range(Student):
        if Student-Student/10 < Score[m] <= Student:
            New_Score[m] ='D0'
        if Student-(Student/10)*2 < Score[m] <= Student-Student/10:
            New_Score[m] ='C-'
        if Student-(Student/10)*3< Score[m] <=Student-(Student/10)*2:
            New_Score[m] ='C0'
        if Student-(Student/10)*4< Score[m] <= Student-(Student/10)*3:
            New_Score[m] ='C+'
        if Student-(Student/10)*5< Score[m] <= Student-(Student/10)*4:
            New_Score[m] ='B-'
        if Student-(Student/10)*6< Score[m] <= Student-(Student/10)*5:
            New_Score[m] ='B0'
        if Student-(Student/10)*7< Score[m] <= Student-(Student/10)*6:
            New_Score[m] ='B+'
        if Student-(Student/10)*8< Score[m] <= Student-(Student/10)*7:
            New_Score[m] ='A-'
        if Student-(Student/10)*9< Score[m] <= Student-(Student/10)*8:
            New_Score[m] ='A0'
        if 0<= Score[m] <= Student-(Student/10)*9:
            New_Score[m] ='A+'
    print(f'#{i+1} {New_Score[Student_num-1]}')
    New_Score=[]
    Score=[]
