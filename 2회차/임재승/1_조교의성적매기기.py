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
    result = (cnt + ((N-1)//10)) // (N//10)
    print(f'#{q} {point[result]}')

# 어거지로 딕셔너리로 풀어보려다가 이렇게됐습니다 ㅠㅠ
# 거의 유니크 그 자체...
# if (li[K-1][0] * 35) + (li[K-1][1] * 45) + (li[K-1][2] * 20) > (li[i][0] * 35) + (li[i][1] * 45) + (li[i][2] * 20):
# 위 코드도 그냥 미리 리스튼=에 저장해둘걸 싶었습니다 ㅎㅎ

# 중간에 point를 딕셔너리가아니라 리스트로해서 진행했으면 좀더 빠르게했을거같은데
# 그냥 한번 해봤습니다...
# result = (cnt + ((N-1)//10)) // (N//10) 이것도 뭔가 좀 어거지로 푼거같고
# 깔끔하고 정돈되게 풀고싶은데 잘 안되네용
