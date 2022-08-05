import sys

sys.stdin = open("_조교의성적매기기.txt")

glade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
# A+부터 D0까지 10개의 등급으로 성적이 나뉘어 집니다.
test_case = int(input())
for test in range(1, test_case + 1):
    people, pos = map(int, input().split())
    # 성적을 매길 사람이 몇 명인지와 알고싶은 사람의 몇 번째에 오는지가 주어졌습니다
    glade2 = []
    for i in range(10):
        glade2+= [glade[i]]*(people // 10)
    # glade와 10의 배수인 사람을 이용하여 사람 수와 동일하게 순위에따라 등급을 매겨줍니다.
    point_list = []

    for i in range(people):    
        mid, fin, repo = map(int, input().split())
        point = mid * 0.35 + fin * 0.45 + repo * 0.2
        point_list.append(point)
    #각 성적을 주어진 계수에 곱한 값을 더하여 빈 리스트에 더해줍니다.
    finding = point_list[pos - 1]
    # 현실에서는 1부터 수를 세지만 인덱스는 0부터 시작이기때문에 주어진 위치에서 1을 뺀 인덱스의 점수를 찾습니다.
    re_point = sorted(point_list, reverse = True)
    a = re_point.index(finding)
    # 성적을 모은 리스트를 내림차순으로 정렬하여 찾은 점수의 인덱스 값으로 다시 만들어준 glade2 리스트에서 성적을 찾습니다.
    print(f'#{test} {glade2[a]}')