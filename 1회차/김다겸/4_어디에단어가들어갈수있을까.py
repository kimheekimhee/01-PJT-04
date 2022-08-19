# import sys

# sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())

for t in range(1, T+1):
    n, k = map(int, input().split())

    arr = [0 for _ in range(n)]

    for i in range(n):    
        arr[i] = list(map(int, input().split()))

    # arr의 맨 윗줄과 아랫줄에 0 리스트 추가
    arr.insert(0, [0] * n)
    arr.insert(n+1, [0] * n)

    # arr의 맨 왼쪽과 오른쪽에 0 추가
    for i in range(n+2):
        arr[i].insert(0, 0)
        arr[i].insert(n+1, 0)

    cnt_list_w = []
    cnt_list_h = []
    ans = 0

    # 가로 순회
    for i in range(1, n+1):
        # cnt를 0으로 초기화
        cnt = 0
        for j in range(1, n+1):
            # arr[i][j]가 1이면
            if arr[i][j] == 1:
                # cnt에 1씩 더하기
                cnt += 1
            # arr[i][j]가 0이면
            if arr[i][j+1] == 0:
                # 가로의 cnt_list에 cnt 추가
                cnt_list_w.append(cnt)
                # cnt 0으로 초기화
                cnt = 0

    # 가로 줄 리스트 순회
    for i in range(len(cnt_list_w)):
        # 가로줄 cnt가 k와 같으면
        if cnt_list_w[i] == k:
            # ans에 1씩 추가
            ans += 1

    # 가로와 똑같이 반복
    for i in range(1, n+1):
        cnt = 0
        for j in range(1, n+1):
            if arr[j][i] == 1:
                cnt += 1
            if arr[j+1][i] == 0:
                cnt_list_h.append(cnt)
                cnt = 0

    for i in range(len(cnt_list_h)):
        if cnt_list_h[i] == k:
            ans += 1
    print(f'#{t} {ans}')