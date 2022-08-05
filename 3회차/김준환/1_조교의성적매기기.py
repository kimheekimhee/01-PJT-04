from genericpath import samestat
import sys

# sys.stdin = open("_조교의성적매기기.txt")

t = int(input())

for test in range(t):
    same_grade = 0
    sum_lst = []
    score_lst = []
    n, k = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    same_grade = n//10
    for col in range(n):
        sum_lst.append(matrix[col][0]*0.35 + matrix[col][1]*0.45 + matrix[col][2]*0.2)
        score_lst.append(matrix[col][0]*0.35 + matrix[col][1]*0.45 + matrix[col][2]*0.2)
    sum_lst.sort()
    if score_lst[k-1] >= sum_lst[-same_grade]:
        result = 'A-'
    elif score_lst[k-1] >= sum_lst[-same_grade*2]:
        result = 'A0'
    elif score_lst[k-1] >= sum_lst[-same_grade*3]:
        result = 'A-'
    elif score_lst[k-1] >= sum_lst[-same_grade*4]:
        result = 'B+'
    elif score_lst[k-1] >= sum_lst[-same_grade*5]:
        result = 'B0'
    elif score_lst[k-1] >= sum_lst[-same_grade*6]:
        result = 'B-'
    elif score_lst[k-1] >= sum_lst[-same_grade*7]:
        result = 'C+'
    elif score_lst[k-1] >= sum_lst[-same_grade*8]:
        result = 'C0'
    elif score_lst[k-1] >= sum_lst[-same_grade*9]:
        result = 'C-'
    else:
        result = 'D0'
    print(f'#{test+1} {result}')