import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())

N, M = map(int, input().split())
score_list =[]
for _ in range(N):
    a, b, c = map(int, input().split())
    score = (a * 0.35) + (b * 0.45) + (c * 0.2)
    score_list.append(score)
    sor_score_list = sorted(score_list)
for i in range(len(sor_score_list)):
    if i < N//10:
        score_list.replace(sor_score_list[i], 'D0')
print(score_list)