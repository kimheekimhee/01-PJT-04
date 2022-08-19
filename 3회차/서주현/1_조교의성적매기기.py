import sys

sys.stdin = open("_조교의성적매기기.txt")


gradedic = {
    1 : 'A+',
    2 : 'A0',
    3 : 'A-',
    4 : 'B+',
    5 : 'B0',
    6 : 'B-',
    7 : 'C+',
    8 : 'C0',
    9 : 'C-',
    10 : 'D0'
}

T = int(input())

for t in range(1, T+1) :
    n, k = list(map(int, input().split()))
    score= []
    save = []
    for i in range(n) :
        a, b, c = list(map(int, input().split()))
        pscore = (a*35)+(b*45)+(c*20)
        save.append([pscore, i])
        score.append(pscore)
    score.sort(reverse = True)
    # print(save)

    for index_ in range(len(score)) :
        for j in save :
            if score[index_] == j[0] and j[1] == (k-1):
                num = index_+1
                # print(num)
                break
    
    for i in range(10) :
        seq = n / 10
        
        if num <= i*seq :
            print(f'#{t} {gradedic[i]}')
            # print(num, n, i, seq)
            break