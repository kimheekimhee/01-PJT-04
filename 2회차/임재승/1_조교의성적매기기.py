import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())

point = {1 : 'A+', 2 : 'A0', 3 : 'A-', 4 : 'B+', 5 : 'B0', 6 : 'B-',
            7 : 'C+', 8 : 'C0', 9 : 'C-', 10 : 'D0' }

for q in range(1, T+1):
    li = []
    N, K = map(int, input().split())
    cnt = N
    for _ in range(N):
        li.append(list(map(int, input().split())))
    for i in range(N):
        if (li[K-1][0] * 35) + (li[K-1][1] * 45) + (li[K-1][2] * 20) > (li[i][0] * 35) + (li[i][1] * 45) + (li[i][2] * 20):
            cnt -= 1
    #...... point 딕셔너리에 넣어줄려고 어거지로 만들었습니다
    result = (cnt + ((N-1)//10)) // (N//10)
    print(f'#{q} {point[result]}')

# 어거지로 딕셔너리로 풀어보려다가 이렇게됐습니다 ㅠㅠ
# 거의 유니크 그 자체...