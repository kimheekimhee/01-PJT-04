import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())
for t in range(1, T+1):
    N, k = map(int, input().split()) # 학생수, 알고싶은 k
    total = []
    num = 1
    for n in range(N):
        score = list(map(int, input().split()))
        #총점 = 중간35 기말 45 과제20의 합을 구해서 total에 append
        score.append(score[0]*0.35 + score[1]*0.45 + score[2]*0.2)
        score.append(num)
        total.append(score)
        #k 와 비교하기 위해서 num: 1~N까지 넣어놓음
        num+=1
    num=0
    #total을 총점total[3]으로 sort
    total.sort(key= lambda x:x[3], reverse=True)
    
    s = len(total) // 10 #동일한 평점 줄 수 있는 학생 수
    for i in range(len(total)):
        if i < s:
            total[i].append('A+')
        elif i < s*2:
            total[i].append('A0')
        elif i < s*2:
            total[i].append('A-')
        elif i < s*3:
            total[i].append('B+')
        elif i < s*4:
            total[i].append('B0')
        elif i < s*5:
            total[i].append('B-')
        elif i < s*6:
            total[i].append('C+')
        elif i < s*7:
            total[i].append('C0')
        elif i < s*8:
            total[i].append('C-')
        else:
            total[i].append('D0')
    
    
    #total을 k로 sort
    total.sort(key= lambda x:x[4])
    
    print(f'#{t} {total[k-1][5]}')
print(total)  