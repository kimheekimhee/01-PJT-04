import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

# 딱 K에 맞는 칸에만 단어가 들어갈 수 있음

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
   
    puzzle = []

    for _ in range(N):
        puzzle.append(list(map(int, input().split())))

    result = []

    # 행
    for i in range(len(puzzle)):
        cnt = 0
        for j in range(len(puzzle[i])):
            # 흰칸(1이면) cnt +1
            if puzzle[i][j]:
                cnt +=1
           
            # 검정(0) 만나면 cnt를 result 리스트에 넣고 0으로 초기화
            else:
                result.append(cnt)
                cnt = 0
        
        # 만약 행의 마지막 숫자가 1이라면 cnt가 저장되지 않으므로 행 탐색이 끝난 후 cnt추가
        result.append(cnt)

    # 열
    for j in range(len(puzzle[0])):
        cnt = 0
        for i in range(len(puzzle)):
            if puzzle[i][j]:
                cnt += 1
            else:
                result.append(cnt)
                cnt = 0
        result.append(cnt)

    # result에서 K의 개수 세기
    ans = 0
    for num in result:
        if num == K:
            ans += 1

    print(f'#{test_case} {ans}')
