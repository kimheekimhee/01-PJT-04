# import sys

# sys.stdin = open("_조교의성적매기기.txt")

grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

T = int(input())
for t in range(1, T+1):
    n, k = map(int, input().split())
    score = []

    for i in range(n):
        mid, final, assign = map(int, input().split())
        score.append(mid * 0.35 + final * 0.45 + assign * 0.2)

    # k의 인덱스 구하기
    k_score = score[k-1]
    # 점수를 내림차순으로
    sorted_score = sorted(score, reverse=True)
    # k의 인덱스를 정렬한 점수 리스트에서 찾아서 n//10으로 나누기
    rank = sorted_score.index(k_score) // (n//10)
    # grade에서 k rank의 인덱스로 정답 찾기
    k_grade = grade[rank]
    print(f'#{t} {k_grade}')