import sys

sys.stdin = open("_조교의성적매기기.txt")

g=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
tc=int(input())
for i in range(tc):
    n,student=map(int, input().split())
    grades={}
    for j in range(n):
        tmp=list(map(int, input().split()))
        grades[j+1]=(tmp[0]*0.35)+(tmp[1]*0.45)+(tmp[2]*0.20)
    grades=sorted(grades.items(),key=lambda x:x[1],reverse=True)
    result=[]
    b=0
    for j in range(0,n,n//10):
            a=0
            for l in range(n//10):
                temp=list(grades[j+a])
                result.append([temp[0],g[b]])
                a+=1
            b+=1
    result.sort()
    print(f'#{i+1}',result[student-1][1])
    
    # {학생번호:성적,...} 형식의 딕셔너리를 성적순으로 정렬함
    # 학생 수가 n명이라면 각 등급은 (n//10)개씩 존재함
    # 학생번호와 등급을 result리스트에 저장함
    

