import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    score_dict = {} # 점수 : 성적
    for i in range(1, N+1) : # N명 학생들
        mid, fin, hw = map(int, input().split())
        score_dict[mid * 0.35 + fin * 0.45 + hw * 0.2] = ''
    # print(score_dict) 디버깅 잘됨
    # 여기서 ''부분에 성적 입력하고 싶은데 어떻게 해야할지 모르겠음.....
    for i in range(N):
        # n을 10으로 나눠서 점수 구분하고 삽입하면 될까요
        # 될듯말듯해서 여기서 두시간 썼습니다....