import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

t = int(input())

for i in range(1, t + 1):
    n, k = map(int, input().split())

    word = []
    fit = []
    result = 0

    for j in range(n):
        word.append(list(map(int, input().split())))

    for j in range(n):
        r_cnt = 0
        c_cnt = 0

        for l in range(n):
            # 행을 기준으로 확인
            if word[j][l] == 1:         # 행에서 글자가 들어갈 수 있는 칸이라면
                r_cnt += 1              # row_count를 하나씩 늘려준다
                if l == n - 1:          # 한 행이 끝까지 반복했다면
                    fit.append(r_cnt)   # 누적된 row_count를 리스트에 저장한다
            else:                       # 끝까지 반복하지 않고 벽을 만났다면
                fit.append(r_cnt)       # 누적된 row_count를 리스트에 저장한다
                r_cnt = 0               # 저장한 뒤 row_count를 0으로 초기화한다

            # 열을 기준으로 확인
            if word[l][j] == 1:         # 행을 기준으로 확인한 방법을
                c_cnt += 1              # 그대로 전치하여 열을 기준으로 확인한다
                if l == n - 1:
                    fit.append(c_cnt)
            else:
                fit.append(c_cnt)
                c_cnt = 0

    for j in fit:
        if j == k:                      # 원하는 길이의 글자와 빈칸의 길이가 같다면
            result += 1                 # 결과를 하나씩 증가시킨다

    print(f'#{i} {result}')
