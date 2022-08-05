import sys

sys.stdin = open("_조교의성적매기기.txt")

glade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

test_case = int(input())
for test in range(1, test_case + 1):
    people, pos = map(int, input().split())

    glade2 = []
    for i in range(10):
        glade2+= [glade[i]]*(people // 10)
    
    point_list = []

    for i in range(people):    
        mid, fin, repo = map(int, input().split())
        point = mid * 0.35 + fin * 0.45 + repo * 0.2
        point_list.append(point)
    
    finding = point_list[pos - 1]
    re_point = sorted(point_list, reverse = True)
    a = re_point.index(finding)
    print(f'#{test} {glade2[a]}')