import sys
sys.stdin = open("_조교의성적매기기.txt")

# idx 값으로 => 백분위 + 학점 반환
def get_percent(rank):
    per =  rank / N # 0.2
    if per <= 0.1:
        return "D0"
    elif per <= 0.2:
        return "C-"
    elif per <= 0.3:
        return "C0"
    elif per <= 0.4:
        return "C+"
    elif per <= 0.5:
        return "B-"
    elif per <= 0.6:
        return "B0"
    elif per <= 0.7:
        return "B+"
    elif per <= 0.8:
        return "A-"
    elif per <= 0.9:
        return "A0"
    elif per <= 1:
        return "A+"
###############################

T = int(input()) # Test case

for t in range(1, T+1):
    N, K = map(int, input().split()) # N: 이번 케이스 학생 수, K: 찾으려는 학생의 번호

    # 점수 변환하여 score[] 저장
    score = []
    for i in range(1, N+1):
        mid, final, hw = map(int, input().split()) # 점수 받기
        mid *= 0.35
        final *= 0.45
        hw *= 0.2
        sum_ = mid + final + hw
        score.append(sum_) 

    # 오름차순 정렬
    arr_score = sorted(score) # [68.95, 72.35, 74.6, 85.5, 85.75, 85.85000000000001, 88.8, 92.55000000000001, 96.25, 99.45]

    # 얻은 점수 -> 오름차순 index -> +1 -> 등수 반환
    rank = arr_score.index(score[K-1]) + 1

    # 주어진 함수에 넣고, 형식에 맞춰 출력
    print(f"#{t} {get_percent(rank)}")
