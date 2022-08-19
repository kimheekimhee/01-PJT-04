import sys

sys.stdin = open("_조교의성적매기기.txt")

# 모르겠다
T = int(input())
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for test_case in range(1, T+1):
    # n = 학생수, k = 학점확인
    n, k = map(int, input().split())
    arr = []
    for i in range(1, n+1):
        a, b, c = map(float, input().split())
        d = (a * 0.35) + (b * 0.45) + (c * 0.2)
        arr.append(d)
# print(arr)
# [74.6, 92.55000000000001, 88.8, 99.45, 72.35, 85.85000000000001, 96.25, 68.95, 85.5, 85.75]
    # k번째 학생의 인덱스를 구해줘서 성적을 매김
    k_score = arr[k-1]
    # 성적을 높은순으로 정렬해줌
    arr.sort(reverse=True)
    final_k_score = arr.index(k_score) // (n//10)
    print(f'#{test_case} {grades[final_k_score]}')