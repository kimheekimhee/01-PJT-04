import sys
from pprint import pprint

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())
ranks = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for _ in range(1, T + 1):
    score_list = []
    n, student_num = map(int, input().split())
    student_list = [list(map(int, input().split())) for _ in range(n)]
    check = 0
    # print(student_list)
    for student in student_list:
        score_list.append(student[0] * 0.35 + student[1] * 0.45 + student[2] * 0.2)
    # pprint(score_list)
    # 몇등인지 확인
    rank = 1
    for i in range(len(score_list)):
        if student_num - 1 != i and score_list[student_num - 1] < score_list[i]:
            rank += 1
    scores = n // 10
    res = scores
    for i in range(10):
        if rank <= res:
            print('#', _, ' ', ranks[i], sep='')
            check = 1
            break
        res += scores
    if check == 0:
        print('#', _, ' ', ranks[9], sep='')