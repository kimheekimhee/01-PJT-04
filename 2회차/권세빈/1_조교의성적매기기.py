import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())
grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

for t in range(1, T+1):
    n, k = map(int,input().split())

    # 총점 리스트
    total = []

    # 학생 수만큼 반복문
    for stu in range(n):
        # 점수 받기
        mid, final, ass = map(int,input().split())
        # 반영 비율대로 총점 계산해서 total 리스트 추가
        total.append((mid*35/100)+(final*45/100)+(ass*20/100))
        # 총점 내림차순으로 정렬
        s_total = sorted(total,reverse=True)

    # 평점 비율 계산
    pct = n//10

    # k의 점수를 이용해 정렬된 총점리스트에서 k의 인덱스 번호(위치) 저장
    k_index = s_total.index(total[k-1])

    # 인덱스 순서대로 비율을 나누면 해당 등급을 계산할 수 있음
    print(f'#{t}',grade[k_index//pct])