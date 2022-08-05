import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())

for tc in range(1, T + 1):
    n, k = map(int, input().split())
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    total_list = []
    cnt = n // 10
    
    for i in range(n):
        mid, final, homework = map(int, input().split())
        total = round(mid * 0.35 + final * 0.45 + homework * 0.2, 2)
        total_list.append(total)
        
    k_total = total_list[k - 1]
    total_list.sort(reverse = True)
    k_rank = total_list.index(k_total) // cnt
    
    print(f'#{tc} {grade[k_rank]}')
