import sys

sys.stdin = open("_조교의성적매기기.txt")

# 테스트케이스 수 변수 선언
T = int(input())

# T 갯수만큼의 테스트케이스 처리
for i in range (1, T+1):
    # 학생 수 N, 학점을 알고싶은 학생번호 K 변수 선언
    N, K = map(int, input().split())

    # 모든 학생의 점수를 담는 리스트 선언
    score_total = []
    
    # K번째 학생의 점수 담는 변수 선언
    score_K = 0

    # 평점(10개) 리스트 선언
    score_list = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

    # 학생별 총 점수 선언
    for j in range(1, N+1):
        mid, fin, hw = map(int, input().split())
        score = (mid*0.35) + (fin*0.45) + (hw*0.2)
        score_total.append(score)

    # K번째 학생의 점수는 따로 저장
        if j == K:
            score_K = score

    # 전체 학생의 점수를 높은 순으로 정렬
    score_total.sort(reverse=True)

    # 상대평가이므로, 학생 수에 따른 K학생의 상대적 위치 구하기
    # 총 학생수 N일때 몇명씩 평점 나누는지 확인
    score_standard = N // 10

    # K번째 학생의 점수 위치를 index로 확인하여 상대적 위치 구하기
    score_list_K = score_total.index(score_K) // score_standard

    # 상대적 위치에 따른 평점 위치 출력(결과값 출력)
    print(f"#{i}", score_list[score_list_K])