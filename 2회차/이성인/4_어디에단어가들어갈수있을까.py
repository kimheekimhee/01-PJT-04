import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle_list = []
    answer = 0
    for _ in  range(N):
        data = input().split()
        puzzle_list.append(data) # 퍼즐판을 만든다. 

    for i in range(N): # 가로를 구하는 식.
        blank_cnt = 0
        for j in range(N):
            if puzzle_list[i][j] == "1": # "1"을 만나면 일단 세고
                blank_cnt += 1
            else: 
                if blank_cnt == K: # "0"을 만나면 K칸인지 확인한다. 
                    answer += 1 # 맞으면 카운트 
                blank_cnt = 0 # 리셋은 무조건
        else:
            if blank_cnt == K: # 마지막 끝났을때 "0"만난거 처럼 해 준다. 
                answer += 1
            blank_cnt = 0


    for i in range(N): # 세로 구하는 식
        blank_cnt = 0
        for j in range(N):
            if puzzle_list[j][i] == "1": # 위 식에서 i,j위치만 바꾸었습니다. 
                blank_cnt += 1
            else: 
                if blank_cnt == K:
                    answer += 1
                blank_cnt = 0
        else:
            if blank_cnt == K:
                answer += 1
            blank_cnt = 0
    print(f"#{t} {answer}")
# 4 6 8 10
# 8 4
# 0 1 1 1 0 1 1 1
# 1 0 0 1 0 1 0 0
# 1 0 0 1 1 1 0 1
# 1 1 1 0 0 1 1 1
# 0 0 1 0 0 1 0 1
# 1 1 1 1 1 0 0 0
# 0 1 0 0 1 0 0 0
# 1 1 1 0 1 1 1 0




    