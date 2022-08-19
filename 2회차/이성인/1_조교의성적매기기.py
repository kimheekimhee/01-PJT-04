import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input()) #이미 푼 문제라서 수월하게 풀 수 있었습니다. 

for t in range(1,T+1):
    score = 0
    score_list = []
    score_list_ranking = []
    credit = ["D0","C-","C0","C+","B-","B0","B+","A-","A0","A+"]
    N, K = map(int, input().split())
    for sco in range(N): 
        a,b,c = map(int, input().split())
        score = (a*35) + (b*45) + (c*20)
        score_list.append(score) # 순서에 맞게 점수를 저장 
    score_list_ranking = sorted(score_list) # 점수를 정렬함 
    # (순서에 맞는 리스트 하나, 정렬된 리스트 하나 생성)

    ranking =(score_list_ranking.index(score_list[K-1]))//(N//10) 
    # index를 사용하면 몇 등인지 알 수 있다.순서리스트에서 k학생 점수를 index
    # (그외는 상수를 활용하여 값을 하나하나 찾아주어 
    # 예를들어 30명 이면 index값이 29,28,27나오면 9, 26,25,24가 나오면 8이 되도록하였습니다. 
    print(f"#{t} {credit[ranking]}") # 해당 학점 부여