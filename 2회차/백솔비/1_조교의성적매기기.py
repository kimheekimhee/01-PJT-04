import sys
sys.stdin = open("_조교의성적매기기.txt")

T = int(input())
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for tc in range(1, T+1):
    N, K = map(int, input().split())
    total = []

    # 학생들의 점수를 구해줍니다.
    for _ in range(N):
        M, F, T = map(int, input().split())
        score = M * 0.35 + F * 0.45 + T * 0.2
        total.append(score)
    
    # K번째 학생을 구해야하는데 컴퓨터는 0부터 세기 때문에 -1을 해줍니다.
    K_score = total[K-1]
    # 성적을 높은 순부터 낮은 순으로 정렬합니다.
    total.sort(reverse=True)

    value = N//10
    # 해당 학점을 받는 학생 수가 정해져 있기 때문에 나누어줍니다.
    result = total.index(K_score)//value

    print(f'#{tc} {grades[result]}')