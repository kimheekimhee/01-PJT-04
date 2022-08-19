import sys

sys.stdin = open("_조교의성적매기기.txt")

for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    grade = []
    for p in range(n):
        mid, last, hw = map(int, input().split())
        total = int(0.35 * mid + 0.45 * last + 0.2 * hw)
        grade.append(total)
    
    grade_arr = sorted(grade)[::-1]
    k_num = 1 + grade_arr.index(grade[k-1]) 
    
    if grade.count(grade[k-1]) > 1:
        k_num += grade.count(grade[k-1]) - 1

    g_num = int(n / 10)
    # g = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    # i = int(k_num // g_num)
    # print(f'#{t} {g[i]}')
    # 이렇게 하면 정답이 안 나오는데 왜 안나오는지 알려주세요..

    if 1 <= k_num < g_num * 1:
        a = 'A+'
    elif k_num < g_num * 2:
        a = 'A0'
    elif k_num < g_num * 3:
        a = 'A-'
    elif k_num < g_num * 4:
        a = 'B+'
    elif k_num < g_num * 5:
        a = 'B0'
    elif k_num < g_num * 6:
        a = 'B-'
    elif k_num < g_num * 7:
        a = 'C+'
    elif k_num < g_num * 8:
        a = 'C0'
    elif k_num < g_num * 9:
        a = 'C-'
    else:
        a = 'D0'

    print(f'#{t} {a}')