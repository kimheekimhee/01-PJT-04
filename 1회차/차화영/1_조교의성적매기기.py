# from pprint import pprint
import sys

sys.stdin = open("_조교의성적매기기.txt")
T = int(input()) # 테스트 케이스의 개수
score_list = []
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for tc in range(1, T+1): # T개의 테스트 케이스를 순회
    a, b = map(int, input().split())  # a : 학생 수, b : 학점을 알고 싶은 학생의 번호
    for _ in range(a):
        중간, 기말, 과제 = map(int, input().split())
        score = 중간 * 0.35 + 기말 * 0.45 + 과제 * 0.2 # 총점 계산
        score_list.append(score) # 리스트에 추가
        score_list.sort(reverse = True) # 바로 출력하면 오름차순 정렬이므로 reverse = True를 통해 내림차순 정렬
        